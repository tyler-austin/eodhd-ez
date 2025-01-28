from typing import *

Period = Literal['1m', '5m', '1h']

USExchange = Literal[
	'US', 'NYSE', 'NASDAQ', 'NYSE MKT', 'BATS', 'NMFQS', 'PINK',
	'OTCQB', 'OTCQX', 'OTCMKTS', 'OTCBB', 'OTCGREY', 'OTC'
]

ExchangeCode = Literal[
	'US', 'TO', 'V', 'NEO', 'BE', 'HM', 'XETRA', 'DU', 'HA', 'MU', 'STU', 'F', 'LU',
	'VI', 'PA', 'BR', 'MC', 'SW', 'LS', 'AS', 'IC', 'IR', 'HE', 'OL', 'CO', 'ST',
	'VFEX', 'XZIM', 'LUSE', 'USE', 'DSE', 'PR', 'RSE', 'XBOT', 'EGX', 'XNSA', 'GSE',
	'MSE', 'BRVM', 'XNAI', 'BC', 'SEM', 'TA', 'KQ', 'KO', 'BUD', 'WAR', 'PSE', 'JK',
	'AU', 'SHG', 'KAR', 'JSE', 'NSE', 'AT', 'SHE', 'SN', 'BK', 'CM', 'VN', 'KLSE',
	'RO', 'SA', 'BA', 'MX', 'IL', 'ZSE', 'TW', 'TWO', 'EUBOND', 'LIM', 'GBOND',
	'MONEY', 'EUFUND', 'IS', 'FOREX', 'CC'
]


class ExchangeFilters(TypedDict):
	Name: Optional[str]
	Code: Optional[ExchangeCode]
	OperatingMIC: Optional[str]
	Country: Optional[str]
	Currency: Optional[str]
	CountryISO2: Optional[str]
	CountryISO3: Optional[str]


SecurityType = Literal[
	'FIND', 'MONEY', 'Rate', 'Notes', 'CommonStock', 'Unit', 'Bond',
	'etf', 'BOND', 'ETF', 'Common Stock', 'Mutual Fund', 'Note', 'CEF',
	'Currency', 'Capital Notes', 'INDEX', 'Preferred Stock', 'FUND',
	'EUFUND', 'ETC', 'Fund'
]


class TickerFilters(TypedDict, total=False):
	Code: Optional[str | List[str]]
	Name: Optional[str | List[str]]
	Country: Optional[str | List[str]]
	Exchange: Optional[str | List[str]]
	Currency: Optional[str | List[str]]
	Type: Optional[SecurityType | List[SecurityType]]
	ISIN: Optional[str | List[str]]
