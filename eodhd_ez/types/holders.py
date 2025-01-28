from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class InstitutionDTO(BaseModel):
	name: Optional[str] = None
	date: Optional[datetime] = None
	total_shares: Optional[float] = None
	total_assets: Optional[float] = None
	current_shares: Optional[int] = None
	change: Optional[int] = None
	change_p: Optional[float] = None


class FundDTO(BaseModel):
	name: Optional[str] = None
	date: Optional[datetime] = None
	total_shares: Optional[float] = None
	total_assets: Optional[float] = None
	current_shares: Optional[int] = None
	change: Optional[int] = None
	change_p: Optional[float] = None


class HoldersDTO(BaseModel):
	institutions: Optional[Dict[str, InstitutionDTO]] = None
	funds: Optional[Dict[str, FundDTO]] = None

