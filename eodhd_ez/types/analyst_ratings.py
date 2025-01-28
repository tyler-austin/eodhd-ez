from typing import Optional

from pydantic import BaseModel


class AnalystRatingsDTO(BaseModel):
    rating: Optional[float] = None
    target_price: Optional[float] = None
    strong_buy: Optional[int] = None
    buy: Optional[int] = None
    hold: Optional[int] = None
    sell: Optional[int] = None
    strong_sell: Optional[int] = None
