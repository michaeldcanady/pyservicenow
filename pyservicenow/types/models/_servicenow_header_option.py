"""Houses Service-Now Header Option"""

from typing import Dict

from pyrestsdk.type.model import HeaderOption
from pyservicenow.types.enums import Header


class ServiceNowHeaderOption(HeaderOption):
    """Service-Now Header Option"""

    Name: Header

    @property
    def as_dict(self) -> Dict[str, str]:
        return {str(self.Name): str(self.Value)}