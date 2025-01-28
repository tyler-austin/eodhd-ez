from eodhd import APIClient

from eodhd_ez import GeneralDTO
from eodhd_ez.types.fundamental_data import FundamentalDataDTO


class FundamentalData(FundamentalDataDTO):
	api: APIClient
	general: GeneralDTO

	def __init__(
			self,
			api: APIClient,
			general: GeneralDTO
	):
		self.api = api
		self.general = general


