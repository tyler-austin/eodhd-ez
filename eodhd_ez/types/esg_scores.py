from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class ActivitiesInvolvementDTO(BaseModel):
	activity: Optional[str] = None
	involvement: Optional[str] = None


class ESGScoresDTO(BaseModel):
	disclaimer: Optional[str] = None
	rating_date: Optional[datetime] = None
	total_esg: Optional[float] = None
	total_esg_percentile: Optional[float] = None
	environment_score: Optional[float] = None
	environment_score_percentile: Optional[int] = None
	social_score: Optional[float] = None
	social_score_percentile: Optional[int] = None
	governance_score: Optional[float] = None
	governance_score_percentile: Optional[int] = None
	controversy_level: Optional[int] = None
	activities_involvement: Optional[Dict[str, ActivitiesInvolvementDTO]] = None
