from typing import Any, Dict, List, Optional, Union

FilterValue = Union[str, List[str]]
Filters = Dict[str, FilterValue]


def filter_match(
		item_value: Optional[Any],
		filter_value: FilterValue
) -> bool:
	item_value_str = str(item_value or '').lower()
	if isinstance(filter_value, list):
		return any(
			str(token).lower() == item_value_str or str(token).lower() in item_value_str
			for token in filter_value
		)
	else:
		return str(filter_value).lower() in item_value_str


def filter_dict_list(
		items: List[Dict[str, Any]],
		filters: Optional[Filters] = None
) -> List[Dict[str, Any]]:
	if not filters:
		return items

	return [
		item for item in items
		if all(
			filter_match(item.get(k, None), v)
			for k, v in filters.items()
			if v not in [None, '', []]
		)
	]
