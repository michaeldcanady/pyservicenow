from pyrestsdk.type.model import QueryOption

# internal imports
from pyservicenow.types.enums import Header

class ServiceNowHeaderOption(QueryOption):

    name: Header

    def __init__(self, name: Header, value: str) -> None:
        super().__init__(name, value)