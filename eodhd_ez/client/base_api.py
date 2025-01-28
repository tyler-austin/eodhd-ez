import json
import logging
from json.decoder import JSONDecodeError
from typing import Optional

import requests
from requests import ConnectionError, HTTPError, Timeout


class BaseAPI:
	API_URL = "https://eodhd.com/api"
	api_key: str
	logger: logging.Logger = None
	session: Optional[requests.Session] = None

	def __init__(
			self,
			api_key: str,
			logger: logging.Logger = None,
			session: Optional[requests.Session] = None,
	):
		self.api_key = api_key
		self.logger = logger
		self.session = session

	def get(self, endpoint: str = "", uri: str = "", querystring: str = "") -> dict:
		try:
			api_path = f"/{endpoint}/{uri}"
			path = f"{self.API_URL}{api_path}"
			url = f"{path}?api_token={self.api_key}&fmt=json{querystring}"

			self.logger.debug(f"[{uri}] Requesting URL: {url}")

			resp = self.session.get(url)

			cache_key = getattr(resp, 'cache_key', None)
			if cache_key:
				self.logger.debug(f"[{uri}] Response Cache Key: {cache_key}")
			else:
				self.logger.debug(f"[{uri}] No cache key found in response")

			cache_hit = getattr(resp, 'from_cache', False)
			if cache_hit:
				self.logger.debug(f"[{uri}] Cache hit: Response served from cache for {path}")
			else:
				self.logger.debug(f"[{uri}] Cache miss: Response fetched from API path {path}")

			status_code = getattr(resp, 'status_code', None)
			if status_code and status_code == 200:
				self.logger.debug(f"[{uri}] Response status: {resp.status_code}, URL: {url}")
			else:
				self.logger.warning(f"[{uri}] Bad Response for URL {url}")
				resp_data = resp.json()
				formatted_content = json.dumps(resp_data, indent=2)
				self.logger.error(f"[{uri}] API Error: {formatted_content}")

			# Try to parse JSON response
			resp.raise_for_status()
			return resp.json()

		except (ConnectionError, HTTPError, Timeout) as err:
			raise err
		except EOFError as err:
			raise err
		except JSONDecodeError as err:
			raise err
		except ValueError as err:
			raise err
		except Exception as err:
			raise err
