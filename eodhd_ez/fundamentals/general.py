import inflection
from eodhd import APIClient

from eodhd_ez.types.general import GeneralDTO


class General(GeneralDTO):
	api: APIClient

	def __init__(self, api: APIClient, data: dict):
		self.api = api

		listings = data.pop('Listings', {})
		officers = data.pop('Officers', {})

		data['listings'] = [v for _, v in listings.items()]
		data['officers'] = [v for _, v in officers.items()]

		data = {inflection.underscore(k): v for k, v in data.items()}
		super().__init__(**data)




