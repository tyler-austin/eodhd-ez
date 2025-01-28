from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HighlightsDTO(BaseModel):
    market_capitalization: Optional[int] = None
    market_capitalization_mln: Optional[float] = None
    ebitda: Optional[int] = None
    pe_ratio: Optional[float] = None
    peg_ratio: Optional[float] = None
    wall_street_target_price: Optional[float] = None
    book_value: Optional[float] = None
    dividend_share: Optional[int] = None
    dividend_yield: Optional[float] = None
    earnings_share: Optional[float] = None
    eps_estimate_current_year: Optional[float] = None
    eps_estimate_next_year: Optional[float] = None
    eps_estimate_next_quarter: Optional[float] = None
    eps_estimate_current_quarter: Optional[float] = None
    most_recent_quarter: Optional[datetime] = None
    profit_margin: Optional[float] = None
    operating_margin_ttm: Optional[float] = None
    return_on_assets_ttm: Optional[float] = None
    return_on_equity_ttm: Optional[float] = None
    revenue_ttm: Optional[int] = None
    revenue_per_share_ttm: Optional[float] = None
    quarterly_revenue_growth_yoy: Optional[float] = None
    gross_profit_ttm: Optional[int] = None
    diluted_eps_ttm: Optional[float] = None
    quarterly_earnings_growth_yoy: Optional[float] = None

