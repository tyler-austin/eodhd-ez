from typing import *

import pandas as pd
from eodhd import APIClient

from eodhd_ez.typing import TickerFilters
from eodhd_ez.utils.filters import filter_dict_list


def get_tickers(
		api: APIClient,
		exchange_code: str,
		delisted: Optional[bool] = False,
		filters: Optional[TickerFilters] = None,
) -> list:
	tickers = api.get_list_of_tickers(
		code=exchange_code,
		delisted=(1 if delisted else 0)
	)
	return filter_dict_list(tickers, filters)


def get_tickers_df(
		api: APIClient,
		exchange_code: str,
		delisted: Optional[bool] = False,
		filters: Optional[TickerFilters] = None,
) -> pd.DataFrame:
	return pd.DataFrame(get_tickers(api, exchange_code, delisted, filters))


