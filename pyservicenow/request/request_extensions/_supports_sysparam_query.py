"""Houses Supports Sysparam Query"""
from typing import Union, TypeVar

from pyrestsdk.request.supports_types import SupportsQueryOptions

from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption, QueryBuilder

S = TypeVar("S", bound="SupportsSysparamQuery")


class SupportsSysparamQuery(SupportsQueryOptions):
    """Supports Sysparam Query Type"""

    def sysparam_query(self: S, query: Union[str, QueryBuilder]) -> S:
        """Encoded query used to filter the result set.
        You can use a UI filter to obtain a properly encoded query.

        Args:
            query (str): Encoded query used to filter the result set.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        # removed until completion of Issue #42
        #if not isinstance(query, QueryBuilder):
        #    query = QueryBuilder.parse(query)

        self.query_options.append(ServiceNowQueryOption(QueryParameters.QUERY, query))

        return self
