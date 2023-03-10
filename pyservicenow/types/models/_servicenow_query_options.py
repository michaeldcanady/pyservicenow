"""Houses Service-Now Query Option"""

from typing import Any, Dict
from pyrestsdk.type.model import QueryOption
from pyservicenow.types.enums import QueryParameters


class ServiceNowQueryOption(QueryOption):
    """Service-Now Query Option type"""

    Name: QueryParameters

    @property
    def as_dict(self) -> Dict[str, Any]:

        if isinstance(self.Value, list):
            return {self.Name: ",".join(self.Value)}
        return {self.Name: self.Value}
