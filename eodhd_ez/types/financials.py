from typing import Dict, Optional

from pydantic import BaseModel

from eodhd_ez.types.enums import Currency


class BalanceSheetReportDTO(BaseModel):
	date: Optional[str] = None
	filing_date: Optional[str] = None
	currency_symbol: Optional[str] = None
	total_assets: Optional[str] = None
	intangible_assets: Optional[str] = None
	earning_assets: Optional[str] = None
	other_current_assets: Optional[str] = None
	total_liab: Optional[str] = None
	total_stockholder_equity: Optional[str] = None
	deferred_long_term_liab: Optional[str] = None
	other_current_liab: Optional[str] = None
	common_stock: Optional[str] = None
	capital_stock: Optional[str] = None
	retained_earnings: Optional[str] = None
	other_liab: Optional[str] = None
	good_will: Optional[str] = None
	other_assets: Optional[str] = None
	cash: Optional[str] = None
	cash_and_equivalents: Optional[str] = None
	total_current_liabilities: Optional[str] = None
	current_deferred_revenue: Optional[str] = None
	net_debt: Optional[str] = None
	short_term_debt: Optional[str] = None
	short_long_term_debt: Optional[str] = None
	short_long_term_debt_total: Optional[str] = None
	other_stockholder_equity: Optional[str] = None
	property_plant_equipment: Optional[str] = None
	total_current_assets: Optional[str] = None
	long_term_investments: Optional[str] = None
	net_tangible_assets: Optional[str] = None
	short_term_investments: Optional[str] = None
	net_receivables: Optional[str] = None
	long_term_debt: Optional[str] = None
	inventory: Optional[str] = None
	accounts_payable: Optional[str] = None
	total_permanent_equity: Optional[str] = None
	noncontrolling_interest_in_consolidated_entity: Optional[str] = None
	temporary_equity_redeemable_noncontrolling_interests: Optional[str] = None
	accumulated_other_comprehensive_income: Optional[str] = None
	additional_paid_in_capital: Optional[str] = None
	common_stock_total_equity: Optional[str] = None
	preferred_stock_total_equity: Optional[str] = None
	retained_earnings_total_equity: Optional[str] = None
	treasury_stock: Optional[str] = None
	accumulated_amortization: Optional[str] = None
	non_currrent_assets_other: Optional[str] = None
	deferred_long_term_asset_charges: Optional[str] = None
	non_current_assets_total: Optional[str] = None
	capital_lease_obligations: Optional[str] = None
	long_term_debt_total: Optional[str] = None
	non_current_liabilities_other: Optional[str] = None
	non_current_liabilities_total: Optional[str] = None
	negative_goodwill: Optional[str] = None
	warrants: Optional[str] = None
	preferred_stock_redeemable: Optional[str] = None
	capital_surpluse: Optional[str] = None
	liabilities_and_stockholders_equity: Optional[str] = None
	cash_and_short_term_investments: Optional[str] = None
	property_plant_and_equipment_gross: Optional[str] = None
	property_plant_and_equipment_net: Optional[str] = None
	accumulated_depreciation: Optional[str] = None
	net_working_capital: Optional[str] = None
	net_invested_capital: Optional[str] = None
	common_stock_shares_outstanding: Optional[str] = None


class CashFlowReportDTO(BaseModel):
	date: Optional[str] = None
	filing_date: Optional[str] = None
	currency_symbol: Optional[str] = None
	investments: Optional[str] = None
	change_to_liabilities: Optional[str] = None
	total_cashflows_from_investing_activities: Optional[str] = None
	net_borrowings: Optional[str] = None
	total_cash_from_financing_activities: Optional[str] = None
	change_to_operating_activities: Optional[str] = None
	net_income: Optional[str] = None
	change_in_cash: Optional[str] = None
	begin_period_cash_flow: Optional[str] = None
	end_period_cash_flow: Optional[str] = None
	total_cash_from_operating_activities: Optional[str] = None
	issuance_of_capital_stock: Optional[str] = None
	depreciation: Optional[str] = None
	other_cashflows_from_investing_activities: Optional[str] = None
	dividends_paid: Optional[str] = None
	change_to_inventory: Optional[str] = None
	change_to_account_receivables: Optional[str] = None
	sale_purchase_of_stock: Optional[str] = None
	other_cashflows_from_financing_activities: Optional[str] = None
	change_to_netincome: Optional[str] = None
	capital_expenditures: Optional[str] = None
	change_receivables: Optional[str] = None
	cash_flows_other_operating: Optional[str] = None
	exchange_rate_changes: Optional[str] = None
	cash_and_cash_equivalents_changes: Optional[str] = None
	change_in_working_capital: Optional[str] = None
	stock_based_compensation: Optional[str] = None
	other_non_cash_items: Optional[str] = None
	free_cash_flow: Optional[str] = None


class IncomeStatementReportDTO(BaseModel):
	date: Optional[str] = None
	filing_date: Optional[str] = None
	currency_symbol: Optional[str] = None
	research_development: Optional[str] = None
	effect_of_accounting_charges: Optional[str] = None
	income_before_tax: Optional[str] = None
	minority_interest: Optional[str] = None
	net_income: Optional[str] = None
	selling_general_administrative: Optional[str] = None
	selling_and_marketing_expenses: Optional[str] = None
	gross_profit: Optional[str] = None
	reconciled_depreciation: Optional[str] = None
	ebit: Optional[str] = None
	ebitda: Optional[str] = None
	depreciation_and_amortization: Optional[str] = None
	non_operating_income_net_other: Optional[str] = None
	operating_income: Optional[str] = None
	other_operating_expenses: Optional[str] = None
	interest_expense: Optional[str] = None
	tax_provision: Optional[str] = None
	interest_income: Optional[str] = None
	net_interest_income: Optional[str] = None
	extraordinary_items: Optional[str] = None
	non_recurring: Optional[str] = None
	other_items: Optional[str] = None
	income_tax_expense: Optional[str] = None
	total_revenue: Optional[str] = None
	total_operating_expenses: Optional[str] = None
	cost_of_revenue: Optional[str] = None
	total_other_income_expense_net: Optional[str] = None
	discontinued_operations: Optional[str] = None
	net_income_from_continuing_ops: Optional[str] = None
	net_income_applicable_to_common_shares: Optional[str] = None
	preferred_stock_and_other_adjustments: Optional[str] = None


class BalanceSheetDTO(BaseModel):
	currency_symbol: Optional[Currency] = None
	quarterly: Optional[Dict[str, BalanceSheetReportDTO]] = None
	yearly: Optional[Dict[str, BalanceSheetReportDTO]] = None


class CashFlowDTO(BaseModel):
	currency_symbol: Optional[Currency] = None
	quarterly: Optional[Dict[str, CashFlowReportDTO]] = None
	yearly: Optional[Dict[str, CashFlowReportDTO]] = None


class IncomeStatementDTO(BaseModel):
	currency_symbol: Optional[Currency] = None
	quarterly: Optional[Dict[str, IncomeStatementReportDTO]] = None
	yearly: Optional[Dict[str, IncomeStatementReportDTO]] = None


class FinancialsDTO(BaseModel):
	balance_sheet: Optional[BalanceSheetDTO] = None
	cash_flow: Optional[CashFlowDTO] = None
	income_statement: Optional[IncomeStatementDTO] = None
