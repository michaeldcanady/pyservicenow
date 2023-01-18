"""Houses Supports No Count"""

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


class SupportsNoCount(SupportsQueryOptions):
    """Supports No Count Type"""

    def no_count(self, no_count: bool) -> Self:
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
