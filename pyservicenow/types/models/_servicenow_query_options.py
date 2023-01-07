"""Houses Service-Now Query Option"""

from typing import Any
from pyrestsdk.type.model import QueryOption
from pyservicenow.types.enums import QueryParameters


class ServiceNowQueryOption(QueryOption):
    """Service-Now Query Option type"""

    Name: QueryParameters
