import logging
from typing import *

import pandas as pd
import requests
from eodhd import APIClient

from eodhd_ez import ExchangeFilters, Period, TickerFilters
from eodhd_ez.client.base_api import BaseAPI
from eodhd_ez.exchanges import get_exchanges, get_exchanges_df
from eodhd_ez.historical_data import get_intraday_historical_data
from eodhd_ez.tickers import get_tickers, get_tickers_df


class EODHDEZClient(object):
	api: APIClient = None
	v2: BaseAPI = None

	def __init__(
			self,
			api_key: str,
			logger: Optional[logging.Logger] = logging.getLogger(__name__),
			session: Optional[requests.Session] = requests.Session()
	):
		self.api = APIClient(api_key)
		self.v2 = BaseAPI(api_key, logger, session)

	def get_exchanges(self, filters: Optional[ExchangeFilters] = None) -> list:
		return get_exchanges(self.api, filters)

	def get_exchanges_df(self, filters: Optional[ExchangeFilters] = None) -> pd.DataFrame:
		return get_exchanges_df(self.api, filters)

	def get_tickers(
			self,
			exchange_code: str,
			delisted: Optional[bool] = False,
			filters: Optional[TickerFilters] = None,
	) -> list:
		return get_tickers(self.api, exchange_code, delisted, filters)

	def get_tickers_df(
			self,
			exchange_code: str,
			delisted: Optional[bool] = False,
			filters: Optional[TickerFilters] = None,
	) -> pd.DataFrame:
		return get_tickers_df(self.api, exchange_code, delisted, filters)

	def get_fundamentals(self, symbol: str) -> dict:
		return self.v2.get(endpoint="fundamentals", uri=symbol)

	def get_intraday_historical_data(
			self, symbol: str,
			interval: Period,
			from_date: Optional[str] = None,
			to_date: Optional[str] = None
	) -> pd.DataFrame:
		return get_intraday_historical_data(self.api, symbol, interval, from_date, to_date)
