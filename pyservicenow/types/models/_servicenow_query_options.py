from typing import Any
from pyrestsdk.type.model import QueryOption

# internal imports
from pyservicenow.types.enums import QueryParameters


class ServiceNowQueryOption(QueryOption):

    Name: QueryParameters
