"""Houses Supports Suppress Pagination Header"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSuppressPaginationHeader")


class SupportsSuppressPaginationHeader(SupportsQueryOptions):
    """Supports Suppress Pagination Header Type"""

    def suppress_pagination_header(self: S, suppress_pagination_header: bool) -> S:
        """Flag that indicates whether to remove the Link header from the response.
        The Link header provides various URLs to relative pages in the
        record set which you can use to paginate the returned record set.

        Args:
            suppress_pagination_header (bool): whether to remove the Link header from the response.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(
            ServiceNowQueryOption(
                QueryParameters.SUPPRESSPAGINATIONHEADER, suppress_pagination_header
            )
        )
        return self
