"""Houses Supports Sysparam Offset"""

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


class SupportsSysparamOffset(SupportsQueryOptions):
    """Supports Sysparam Offset Type"""

    def sysparam_offset(self, offset: int) -> Self:
        """Starting record index for which to begin retrieving records.
        Use this value to paginate record retrieval.
        This functionality enables the retrieval of all records,
        regardless of the number of records,
        in small manageable chunks.

        Args:
            offset (int): Starting record index for which to begin retrieving records

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.OFFSET, offset)
        )
        return self
