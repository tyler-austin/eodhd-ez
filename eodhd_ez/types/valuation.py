from typing import Optional

from pydantic import BaseModel


class ValuationDTO(BaseModel):
    trailing_pe: Optional[float] = None
    forward_pe: Optional[float] = None
    price_sales_ttm: Optional[float] = None
    price_book_mrq: Optional[float] = None
    enterprise_value: Optional[int] = None
    enterprise_value_revenue: Optional[float] = None
    enterprise_value_ebitda: Optional[float] = None
