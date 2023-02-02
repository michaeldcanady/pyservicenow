"""Houses Supports Sysparam Limit"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamLimit")


class SupportsSysparamLimit(SupportsQueryOptions):
    """Supports Sysparam Limit Types"""

    def sysparam_limit(self: S, limit: int) -> S:
        """Sets the limit

        Args:
            limit (int): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(ServiceNowQueryOption(QueryParameters.LIMIT, limit))
        return self
