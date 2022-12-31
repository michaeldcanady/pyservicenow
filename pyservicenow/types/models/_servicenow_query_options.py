from typing import Iterable, Dict, Any
from pyrestsdk.type.model import QueryOption

# internal imports
from pyservicenow.types.enums import QueryParameters

class ServiceNowQueryOption(QueryOption):

    name: QueryParameters

    def __init__(self, name: QueryParameters, value: str) -> None:
        super().__init__(name, value)