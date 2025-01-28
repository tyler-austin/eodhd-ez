from typing import Optional

from pydantic import BaseModel


class TechnicalsDTO(BaseModel):
	beta: Optional[float] = None
	week_52_high: Optional[float] = None
	week_52_low: Optional[float] = None
	day_50_ma: Optional[float] = None
	day_200_ma: Optional[float] = None
	shares_short: Optional[int] = None
	shares_short_prior_month: Optional[int] = None
	short_ratio: Optional[float] = None
	short_percent: Optional[float] = None
