"""Houses Supports Sysparam Offset"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamOffset")


class SupportsSysparamOffset(SupportsQueryOptions):
    """Supports Sysparam Offset Type"""

    def sysparam_offset(self: S, offset: int) -> S:
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

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.OFFSET, offset)
        )
        return self
