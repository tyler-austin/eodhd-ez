from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel

from eodhd_ez.types.enums import BeforeAfterMarket, Currency


class EarningsAnnualDTO(BaseModel):
	date: Optional[datetime] = None
	eps_actual: Optional[float] = None


class EarningsHistoryDTO(BaseModel):
	report_date: Optional[datetime] = None
	date: Optional[datetime] = None
	before_after_market: Optional[BeforeAfterMarket] = None
	currency: Optional[Currency] = None
	eps_actual: Optional[float] = None
	eps_estimate: Optional[float] = None
	eps_difference: Optional[float] = None
	surprise_percent: Optional[float] = None


class EarningsTrendDTO(BaseModel):
	date: Optional[datetime] = None
	period: Optional[str] = None
	growth: Optional[str] = None
	earnings_estimate_avg: Optional[str] = None
	earnings_estimate_low: Optional[str] = None
	earnings_estimate_high: Optional[str] = None
	earnings_estimate_year_ago_eps: Optional[str] = None
	earnings_estimate_number_of_analysts: Optional[str] = None
	earnings_estimate_growth: Optional[str] = None
	revenue_estimate_avg: Optional[str] = None
	revenue_estimate_low: Optional[str] = None
	revenue_estimate_high: Optional[str] = None
	revenue_estimate_year_ago_eps: Optional[str] = None
	revenue_estimate_number_of_analysts: Optional[str] = None
	revenue_estimate_growth: Optional[str] = None
	eps_trend_current: Optional[str] = None
	eps_trend7_days_ago: Optional[str] = None
	eps_trend30_days_ago: Optional[str] = None
	eps_trend60_days_ago: Optional[str] = None
	eps_trend90_days_ago: Optional[str] = None
	eps_revisions_up_last7_days: Optional[str] = None
	eps_revisions_up_last30_days: Optional[str] = None
	eps_revisions_down_last7_days: Optional[str] = None
	eps_revisions_down_last30_days: Optional[str] = None


class EarningsDTO(BaseModel):
	annual: Optional[Dict[str, EarningsAnnualDTO]] = None
	history: Optional[Dict[str, EarningsHistoryDTO]] = None
	trend: Optional[Dict[str, EarningsTrendDTO]] = None

