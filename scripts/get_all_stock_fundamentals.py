import json
import logging
import os
import queue
import shutil
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime as dt
from datetime import timezone as tz
from json import JSONDecodeError
from logging import FileHandler, Formatter, StreamHandler
from logging.handlers import QueueHandler, QueueListener
from pathlib import Path

import backoff
import requests
from colorlog import ColoredFormatter
from dotenv import load_dotenv
from ratelimit import limits, sleep_and_retry
from requests import HTTPError, RequestException, Timeout
from requests_cache import CachedSession, RedisCache, json_serializer

from eodhd_ez import EODHDEZClient, TickerFilters

# Set debug mode
debug = True

# Set up directories
repo_dir = '/Users/tyler.austin/Github/eodhd-ez'
logging_dir = os.path.join(repo_dir, 'logs')
os.makedirs(logging_dir, exist_ok=True)
data_dir = os.path.join(repo_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
listings_dir = os.path.join(data_dir, 'listings')
os.makedirs(listings_dir, exist_ok=True)
fundamentals_dir = os.path.join(data_dir, 'fundamentals')
os.makedirs(fundamentals_dir, exist_ok=True)

# Set the logging formatter converter to use UTC time
logging.Formatter.converter = time.gmtime

# Configure FileHandler
now = dt.now(tz.utc).strftime('%Y%m%d_%H%M%S')
log_filename = os.path.join(logging_dir, f"fundamental_data_fetcher_{now}.log")
file_handler = FileHandler(log_filename)
file_formatter = Formatter(
	'[%(asctime)s][%(levelname)s] %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S %Z',
)
file_handler.setFormatter(file_formatter)

# Configure Colorlog's ColoredFormatter
color_formatter = ColoredFormatter(
	"%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
	log_colors={
		"DEBUG": "cyan",
		"INFO": "green",
		"WARNING": "yellow",
		"ERROR": "red",
		"CRITICAL": "bold_red",
	},
)
color_handler = StreamHandler()
color_handler.setFormatter(color_formatter)

# Create a log queue and a QueueListener with handlers
log_queue = queue.Queue(-1)  # No limit on size
queue_handler = QueueHandler(log_queue)
listener = QueueListener(log_queue, file_handler, color_handler)

# Add handlers to the logger
logger = logging.getLogger('EODHDEZ')
LOG_LEVEL = logging.DEBUG if debug else logging.INFO
logger.setLevel(LOG_LEVEL)
logger.addHandler(queue_handler)

# Start the listener
listener.start()

# Initialize logger and queue listener
logger.info(f"Logger initialized: {log_filename}")

# Configure Redis connection parameters
redis_backend = RedisCache(
	host='localhost',  # Redis server address
	port=6379,  # Redis server port
	db=0,  # Redis database index
	ttl=False,  # Disable Redis's internal TTL
	serializer=json_serializer  # Use JSON serialization
)

# Initialize a session with the configured Redis backend
session_cache = CachedSession(
	backend=redis_backend,  # Use Redis as the cache backend
	cache_control=True,  # Use Cache-Control headers for expiration
	expire_after=60 * 60 * 24  # Set expiration to 24 hours
)

logger.info(f"Request Cache Redis backend initialized: {redis_backend}")

# Global variables
load_dotenv()
api_key = os.environ.get('EODHD_API_KEY')
ez = EODHDEZClient(api_key, session=session_cache, logger=logger)


def write_json_file(file_path, data):
	try:
		path_obj = Path(file_path)
		json_str = json.dumps(data, indent=2)
		path_obj.write_text(json_str, encoding='utf-8')
	except Exception as err:
		logger.error(f"Error writing JSON file: {err}")


@sleep_and_retry
@limits(calls=8, period=1)
@limits(calls=500, period=60)
def fetch_data(full_ticker):
	return ez.get_fundamentals(symbol=full_ticker)


@backoff.on_exception(
	backoff.expo,
	RequestException,
	max_tries=10,
	jitter=backoff.full_jitter,
	giveup=lambda x: x.response is not None and x.response.status_code != 429,
)
def fetch_and_save(item, save_dir):
	full_ticker = f"{item}.US"
	fundamentals_file_name = f"{item}.json"
	fundamentals_file_path = os.path.join(save_dir, fundamentals_file_name)
	os.makedirs(os.path.dirname(fundamentals_file_path), exist_ok=True)

	try:
		data = fetch_data(full_ticker)
		write_json_file(fundamentals_file_path, data)
		logger.info(f"[{item}] Successfully fetched and saved fundamental data")
		return True
	except (RequestException, ConnectionError, HTTPError, Timeout) as req_err:
		logger.error(f"[{item}] Request failed: {req_err}")
		return False
	except JSONDecodeError as json_err:
		logger.error(f"[{item}] JSON decoding error: {json_err}")
		return False
	except ValueError as val_err:
		logger.error(f"[{item}] Unexpected ValueError: {val_err}")
		return False
	except Exception as unknown_err:
		logger.error(f"[{item}] Unexpected error: {unknown_err}")
		return False


def fetch_listings_df():
	filters: TickerFilters = {
		"Exchange": [
			"NYSE",
			"NYSE ARCA",
			"AMEX",
			"NMFQS",
			"BATS",
			"NASDAQ",
			"NYSE MKT",
			"US",
		],
		"Type": [
			"Common Stock",
		],
	}
	df = ez.get_tickers_df(exchange_code='US', delisted=False, filters=filters)
	df = df.dropna(subset=['Code'])
	return df


def get_tickers(input_dir: str, date_str: str):
	try:
		listings_df = fetch_listings_df()
		listings_file_path = os.path.join(input_dir, f'{date_str}_listings.csv')
		listings_df.to_csv(listings_file_path)
		logger.info(f'Ticker listings saved to {listings_file_path}')
		tickers_lst = listings_df['Code'].tolist()
		logger.info(f"Successfully fetched ticker listings for {len(tickers_lst)} tickers")
		return tickers_lst
	except requests.exceptions.RequestException as request_err:
		logger.error(f"Network-related error while fetching ticker listings: {request_err}")
		raise request_err
	except Exception as unknown_err:
		raise unknown_err


def main():
	daily_date_str = dt.now(tz.utc).strftime('%Y%m%d')
	daily_dir = os.path.join(fundamentals_dir, f'{daily_date_str}')

	# Remove existing fundamentals directory and create a new one
	if debug and os.path.exists(daily_dir):
		shutil.rmtree(daily_dir)
	os.makedirs(daily_dir, exist_ok=True)

	tickers = get_tickers(listings_dir, daily_date_str)

	# Determine the number of threads to use
	num_threads = 10
	logger.info(f"Using {num_threads} threads to fetch data")

	failed_tickers = []

	try:
		with ThreadPoolExecutor(max_workers=num_threads) as executor:
			future_to_item = {
				executor.submit(fetch_and_save, ticker, daily_dir): ticker
				for ticker in tickers
			}

			for future in as_completed(future_to_item):
				item = future_to_item[future]
				try:
					success = future.result()
					if not success:
						failed_tickers.append(item)
				except Exception as unknown_err:
					logger.error(f"Unhandled exception for item {item}: {unknown_err}")

		if failed_tickers:
			logger.warning(f"Failed to fetch data for {len(failed_tickers)} tickers.")
			with open(os.path.join(logging_dir, f'{daily_date_str}_failed_tickers.txt'), 'w') as f:
				for ticker in failed_tickers:
					f.write(f"{ticker}\n")

		logger.info("Data fetching process completed")
		logger.info(f'Data saved to {daily_dir}')

	except KeyboardInterrupt:
		logger.info("Process interrupted by user. Shutting down...")
		executor.shutdown(wait=False, cancel_futures=True)
		raise

	finally:
		listener.stop()


if __name__ == "__main__":
	main()
