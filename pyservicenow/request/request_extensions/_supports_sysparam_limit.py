"""Houses Supports Sysparam Limit"""

from sys import version_info


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class SupportsSysparamLimit(SupportsQueryOptions):
    """Supports Sysparam Limit Types"""

    def sysparam_limit(self, limit: int) -> Self:
        """Sets the limit

        Args:
            limit (int): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.LIMIT, limit))
        return self
