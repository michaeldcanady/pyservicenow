from typing import Protocol
from sys import version_info


from pyrestsdk.type.model import QueryOptionCollection

class SupportsQueryOptions(Protocol):
    
    __slots__ = ["_query_options"]
    
    _query_options: QueryOptionCollection
    
    def __init__(self) -> None:
        self._query_options = QueryOptionCollection()