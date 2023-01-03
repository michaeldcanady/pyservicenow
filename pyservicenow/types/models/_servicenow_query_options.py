from typing import Any
from pyrestsdk.type.model import QueryOption

# internal imports
from pyservicenow.types.enums import QueryParameters

class ServiceNowQueryOption(QueryOption):

    name: QueryParameters

    def __init__(self, name: QueryParameters, value: Any) -> None:
        super().__init__(name, value)
