from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class OutstandingSharesReportDTO(BaseModel):
	date: Optional[int] = None
	date_formatted: Optional[datetime] = None
	shares_mln: Optional[str] = None
	shares: Optional[int] = None


class OutstandingSharesDTO(BaseModel):
	annual: Optional[Dict[str, OutstandingSharesReportDTO]] = None
	quarterly: Optional[Dict[str, OutstandingSharesReportDTO]] = None
