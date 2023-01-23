"""Houses Supports No Count"""

from typing import TypeVar

from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

S = TypeVar("S", bound="SupportsNoCount")


class SupportsNoCount(SupportsQueryOptions):
    """Supports No Count Type"""

    def no_count(self: S, no_count: bool) -> S:
        """Flag that indicates whether to execute a select count(*)
        query on the table to return the number of rows in the associated table.

        Args:
            no_count (bool): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.NOCOUNT, no_count)
        )
        return self
