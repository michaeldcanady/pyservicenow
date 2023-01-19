"""Houses Supports Query Options"""

from typing import Protocol


from pyrestsdk.type.model import QueryOptionCollection


class SupportsQueryOptions(Protocol):
    """Supports Query Options Type"""

    __slots__ = ["_query_options"]

    _query_options: QueryOptionCollection

    def __init__(self) -> None:
        self._query_options = QueryOptionCollection()
