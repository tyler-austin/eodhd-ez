from datetime import datetime as dt
from typing import *

from dateutil.relativedelta import relativedelta

from eodhd_ez import Period


def get_max_days_from_period(period: Period):
	periods = {'1m': 120, '5m': 600, '1h': 7200}
	return periods[period]


def get_max_interval_dates(period: Period, to_date: Optional[str] = None):
	end_date = dt.strptime(to_date, '%Y-%m-%d') if to_date is not None else dt.now()
	days = get_max_days_from_period(period)
	start_date = end_date - relativedelta(days=days)
	return int(start_date.timestamp()), int(end_date.timestamp())
