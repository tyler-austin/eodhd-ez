from typing import Optional

import pandas as pd

from eodhd_ez.typing import ExchangeFilters
from eodhd_ez.utils.filters import filter_dict_list


def get_exchanges(api, filters: Optional[ExchangeFilters] = None) -> list:
	exchanges = api.get_list_of_exchanges()
	return filter_dict_list(exchanges, filters)


def get_exchanges_df(api, filters: Optional[ExchangeFilters] = None) -> pd.DataFrame:
	return pd.DataFrame(get_exchanges(api, filters)).dropna()
