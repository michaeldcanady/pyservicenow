from typing import Iterable, Dict
from pyrestsdk.type.model import HeaderOption

# internal imports
from pyservicenow.types.enums import Header

class ServiceNowHeaderOption(HeaderOption):

    name: Header

    def __init__(self, name: Header, value: str) -> None:
        super().__init__(name, value)

    def asDict(self) -> Dict:
        return {
            "name": self.Name,
            "value": self.Value
            }

    def __iter__(self) -> Iterable:
        return iter(self.asDict().items())