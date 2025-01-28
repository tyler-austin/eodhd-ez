from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InsiderTransactionDTO(BaseModel):
    date: Optional[datetime] = None
    owner_cik: Optional[str] = None
    owner_name: Optional[str] = None
    transaction_date: Optional[datetime] = None
    transaction_code: Optional[str] = None
    transaction_amount: Optional[int] = None
    transaction_price: Optional[float] = None
    transaction_acquired_disposed: Optional[str] = None
    post_transaction_amount: Optional[int] = None
    sec_link: Optional[str] = None
