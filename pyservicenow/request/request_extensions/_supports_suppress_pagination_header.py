"""Houses Supports Suppress Pagination Header"""

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


class SupportsSuppressPaginationHeader(SupportsQueryOptions):
    """Supports Suppress Pagination Header Type"""

    def suppress_pagination_header(self, suppress_pagination_header: bool) -> Self:
        """Flag that indicates whether to remove the Link header from the response.
        The Link header provides various URLs to relative pages in the
        record set which you can use to paginate the returned record set.

        Args:
            suppress_pagination_header (bool): whether to remove the Link header from the response.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(
                QueryParameters.SUPPRESSPAGINATIONHEADER, suppress_pagination_header
            )
        )
        return self
