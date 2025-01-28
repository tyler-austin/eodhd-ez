from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class NumberDividendsByYearDTO(BaseModel):
	year: Optional[int] = None
	count: Optional[int] = None


class SplitsDividendsDTO(BaseModel):
	forward_annual_dividend_rate: Optional[float] = None
	forward_annual_dividend_yield: Optional[float] = None
	payout_ratio: Optional[float] = None
	dividend_date: Optional[datetime] = None
	ex_dividend_date: Optional[datetime] = None
	last_split_factor: Optional[str] = None
	last_split_date: Optional[datetime] = None
	number_dividends_by_year: Optional[Dict[str, NumberDividendsByYearDTO]] = None

