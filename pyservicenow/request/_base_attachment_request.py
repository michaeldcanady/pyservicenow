"""Houses base attachment request"""

from __future__ import annotations
from typing import Union, TypeVar
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    AttachmentEntry,
)
from pyservicenow.types.models import QueryBuilder

T = TypeVar("T", bound="BaseAttachmentRequest")
A = TypeVar("A", bound=AttachmentEntry)


class BaseAttachmentRequest(BaseServiceNowEntryRequest[A]):
    """Base Attachment Request type"""

    def Limit(self: T, limit: int) -> T:
        """Sets the limit

        Args:
            limit (int): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.LIMIT, limit))
        return self

    def Offset(self: T, offset: int) -> T:
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

    def Query(self: T, query: Union[str, QueryBuilder]) -> T:
        """Encoded query used to filter the result set.
        You can use a UI filter to obtain a properly encoded query.

        Args:
            query (str): Encoded query used to filter the result set.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.QUERY, query))

        return self
