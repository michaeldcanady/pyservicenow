"""Houses Service-Now Header Option"""

from pyrestsdk.type.model import HeaderOption
from pyservicenow.types.enums import Header


class ServiceNowHeaderOption(HeaderOption):
    """Service-Now Header Option"""

    name: Header

    def __init__(self, name: Header, value: str) -> None:
        super().__init__(name, value)
