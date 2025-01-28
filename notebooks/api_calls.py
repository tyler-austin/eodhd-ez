import logging
import sys
from json.decoder import JSONDecodeError
from typing import Optional

import requests
from requests import ConnectionError, HTTPError, Timeout


class BaseAPI:
	API_URL = "https://eodhd.com/api"
	api_key: str
	logger: logging.Logger = logging.getLogger(__name__)
	session: Optional[requests.Session] = None

	def __init__(
			self,
			api_key: str,
			logger: logging.Logger,
			session: Optional[requests.Session] = None
	):
		self.api_key = api_key
		self.logger = logger
		self.session = session or requests.Session()

	def get(self, api_key: str, endpoint: str = "", uri: str = "", querystring: str = ""):
		try:
			resp = self.session.get(f"{self.API_URL}/{endpoint}/{uri}?api_token={api_key}&fmt=json{querystring}")

			if resp.status_code != 200:
				try:
					if "message" in resp.json():
						resp_message = resp.json()["message"]
					elif "errors" in resp.json():
						self.logger.error(resp.json())
						sys.exit(1)
					else:
						resp_message = "Unknown response"

					message = f"({resp.status_code}) {self.API_URL} - {resp_message}"
					self.logger.info(message)

				except JSONDecodeError as err:
					self.logger.error(err)

			try:
				resp.raise_for_status()
				return resp.json()
			except ValueError as err:
				self.logger.error(err)

		except ConnectionError as err:
			self.logger.error(err)
		except HTTPError as err:
			self.logger.error(err)
		except Timeout as err:
			self.logger.error(err)
		return {}
