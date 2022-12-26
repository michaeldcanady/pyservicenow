from __future__ import annotations
from typing import Union, TypeVar, Type, TYPE_CHECKING, Iterable, List
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.types.enums import QueryParameters, DisplayValue, View
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models.querybuilder import QueryBuilder
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowEntry, ServiceNowHeaderOption

T = TypeVar("T", bound='BaseTableRequest')
S = TypeVar("S", bound='ServiceNowEntry')

class BaseTableRequest(BaseServiceNowEntryRequest):

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(_return_type, request_url, client, options)

    # def SysparmDisplayValue(self, value: str)

    def ExcludeReferenceLink(self: T, exclude_reference_link: bool) -> T:
        """Adds if to exclude reference links

        Args:
            exclude_reference_link (bool): If to exclude reference links

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.ExcludeReferenceLink, exclude_reference_link))
        return self

    def DisplayValue(self: T, values: DisplayValue) -> T:
        """Sets the sysparm_display_value

        Args:
            values (DisplayValue): The display values

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.DisplayValue, values))
        return self

    def Fields(self: T, fields: List[str]) -> T:
        """Adds the listed fields

        Args:
            fields (List[str]): The fields to be returned

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.Fields, fields))
        return self

    def Limit(self: T, limit: int) -> T:
        """Sets the limit

        Args:
            limit (int): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """
        
        self._query_options.append(ServiceNowQueryOption(QueryParameters.Limit, limit))
        return self

    def NoCount(self: T, no_count: bool) -> T:
        """Flag that indicates whether to execute a select count(*) query on the table to return the number of rows in the associated table.

        Args:
            no_count (bool): The number of records limit

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.NoCount, no_count))
        return self

    def Offset(self: T, offset: int) -> T:
        """Starting record index for which to begin retrieving records. Use this value to paginate record retrieval.
        This functionality enables the retrieval of all records, regardless of the number of records, in small manageable chunks.

        Args:
            offset (int): Starting record index for which to begin retrieving records

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.Offset, offset))
        return self

    def Query(self: T, query: Union[str, QueryBuilder]) -> T:
        """Encoded query used to filter the result set. You can use a UI filter to obtain a properly encoded query.

        Args:
            query (str): Encoded query used to filter the result set.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """
        #TODO: parse str into query builder (check)
        self._query_options.append(ServiceNowQueryOption(QueryParameters.Query, query))

        return self

    def Category(self: T, category: str) -> T:
        """Name of the category to use for queries.

        Args:
            category (str): Name of the category.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.Category, category))
        return self

    def NoDomain(self: T, no_domain: bool) -> T:
        """Flag that indicates whether to restrict the record search to only the domains for which the logged in user is configured.

        Args:
            no_domain (bool): whether to restrict the record search to only the domains for which the logged in user is configured.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.NoDomain, no_domain))
        return self

    def SuppressPaginationHeader(self: T, suppress_pagination_header: bool) -> T:
        """Flag that indicates whether to remove the Link header from the response.
        The Link header provides various URLs to relative pages in the record set which you can use to paginate the returned record set.

        Args:
            suppress_pagination_header (bool): whether to remove the Link header from the response.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.SuppressPaginationHeader, suppress_pagination_header))
        return self

    def View(self: T, view: View) -> T:
        """UI view for which to render the data. Determines the fields returned in the response.

        Args:
            view (View): The view.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.View, view))
        return self