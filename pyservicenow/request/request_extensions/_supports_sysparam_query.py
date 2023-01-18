from typing import Union
from sys import version_info


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption, QueryBuilder
from pyservicenow.request.request_extensions._supports_query_options import SupportsQueryOptions

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class SupportsSysparamQuery(SupportsQueryOptions):
    
    def sysparam_query(self, query: Union[str, QueryBuilder]) -> Self:
        """Encoded query used to filter the result set.
        You can use a UI filter to obtain a properly encoded query.

        Args:
            query (str): Encoded query used to filter the result set.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.QUERY, query))

        return self