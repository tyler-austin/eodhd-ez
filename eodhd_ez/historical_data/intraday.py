from datetime import datetime as dt
from typing import *

import pandas as pd
from eodhd import APIClient

from eodhd_ez import Period
from eodhd_ez.utils import get_max_interval_dates


def get_intraday_historical_data(
		api: APIClient,
		symbol: str,
		interval: Period,
		from_date: Optional[str] = None,
		to_date: Optional[str] = None
) -> pd.DataFrame:
	if from_date is not None and to_date is not None:
		from_unix_time = int(dt.strptime(from_date, '%Y-%m-%d').timestamp())
		to_unix_time = int(dt.strptime(to_date, '%Y-%m-%d').timestamp())
	else:
		from_unix_time, to_unix_time = get_max_interval_dates(interval, to_date)

	data = api.get_intraday_historical_data(
		symbol=symbol,
		interval=interval,
		from_unix_time=from_unix_time,
		to_unix_time=to_unix_time,
	)
	return pd.DataFrame(data).dropna()
