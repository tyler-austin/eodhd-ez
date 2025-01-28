from typing import Optional

from pydantic import BaseModel


class SharesStatsDTO(BaseModel):
    shares_outstanding: Optional[int] = None
    shares_float: Optional[int] = None
    percent_insiders: Optional[float] = None
    percent_institutions: Optional[float] = None
    shares_short: Optional[int] = None
    shares_short_prior_month: Optional[int] = None
    short_ratio: Optional[float] = None
    short_percent_outstanding: Optional[float] = None
    short_percent_float: Optional[float] = None
