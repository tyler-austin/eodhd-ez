from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class AddressDataDTO(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None


class ListingDTO(BaseModel):
    code: Optional[str] = None
    exchange: Optional[str] = None
    name: Optional[str] = None


class OfficerDTO(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    year_born: Optional[str] = None


class GeneralDTO(BaseModel):
    code: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    exchange: Optional[str] = None
    currency_code: Optional[str] = None
    currency_name: Optional[str] = None
    currency_symbol: Optional[str] = None
    country_name: Optional[str] = None
    country_iso: Optional[str] = None
    open_figi: Optional[str] = None
    isin: Optional[str] = None
    lei: Optional[str] = None
    primary_ticker: Optional[str] = None
    cusip: Optional[int] = None
    cik: Optional[int] = None
    employer_id_number: Optional[str] = None
    fiscal_year_end: Optional[str] = None
    ipo_date: Optional[datetime] = None
    international_domestic: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None
    gic_sector: Optional[str] = None
    gic_group: Optional[str] = None
    gic_industry: Optional[str] = None
    gic_sub_industry: Optional[str] = None
    home_category: Optional[str] = None
    is_delisted: Optional[bool] = None
    description: Optional[str] = None
    address: Optional[str] = None
    address_data: Optional[AddressDataDTO] = None
    listings: Optional[Dict[str, ListingDTO]] = None
    officers: Optional[Dict[str, OfficerDTO]] = None
    phone: Optional[str] = None
    web_url: Optional[str] = None
    logo_url: Optional[str] = None
    full_time_employees: Optional[int] = None
    updated_at: Optional[datetime] = None
