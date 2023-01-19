"""Houses Service-Now Header Option"""

from pyrestsdk.type.model import HeaderOption
from pyservicenow.types.enums import Header


class ServiceNowHeaderOption(HeaderOption):
    """Service-Now Header Option"""

    Name: Header
