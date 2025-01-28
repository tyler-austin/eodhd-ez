from typing import Dict, Optional

from pydantic import BaseModel

from eodhd_ez.types.analyst_ratings import AnalystRatingsDTO
from eodhd_ez.types.esg_scores import ESGScoresDTO
from eodhd_ez.types.general import GeneralDTO
from eodhd_ez.types.highlights import HighlightsDTO
from eodhd_ez.types.holders import HoldersDTO
from eodhd_ez.types.insider_transactions import InsiderTransactionDTO
from eodhd_ez.types.outstanding_shares import OutstandingSharesDTO
from eodhd_ez.types.shares_stats import SharesStatsDTO
from eodhd_ez.types.splits_dividends import SplitsDividendsDTO
from eodhd_ez.types.technicals import TechnicalsDTO
from eodhd_ez.types.valuation import ValuationDTO


class FundamentalDataDTO(BaseModel):
	general: Optional[GeneralDTO] = None
	highlights: Optional[HighlightsDTO] = None
	valuation: Optional[ValuationDTO] = None
	shares_stats: Optional[SharesStatsDTO] = None
	technicals: Optional[TechnicalsDTO] = None
	splits_dividends: Optional[SplitsDividendsDTO] = None
	analyst_ratings: Optional[AnalystRatingsDTO] = None
	holders: Optional[HoldersDTO] = None
	insider_transactions: Optional[Dict[str, InsiderTransactionDTO]] = None
	esg_scores: Optional[ESGScoresDTO] = None
	outstanding_shares: Optional[OutstandingSharesDTO] = None
