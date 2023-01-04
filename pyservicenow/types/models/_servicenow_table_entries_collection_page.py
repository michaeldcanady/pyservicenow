from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
    from pyservicenow.request._table_entry_collection_request import TableEntryCollectionRequest

from requests import Response

# internal imports
from pyservicenow.types.models._collection_page import CollectionPage
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry

class ServiceNowTableEntriesCollectionPage(CollectionPage[ServiceNowEntry]):

    def __init__(self, client) -> None:
        super().__init__(client)

    def InitializeNextPageRequest(self, client: ServiceNowClient, next_page_link_string: str) -> None:
        """Initializes the NextPageRequest property

        Args:
            client (_type_): _description_
            next_page_link_string (str): _description_
        """
        
        self._next_page_request = self.InitializePageRequest(client, next_page_link_string)

    def InitializePreviousPageRequest(self, client: ServiceNowClient, next_page_link_string: str) -> None:
        """Initializes the NextPageRequest property

        Args:
            client (_type_): _description_
            next_page_link_string (str): _description_
        """
        
        self._prev_page_request = self.InitializePageRequest(client, next_page_link_string)

    def InitializeFirstPageRequest(self, client: ServiceNowClient, next_page_link_string: str) -> None:
        """Initializes the NextPageRequest property

        Args:
            client (_type_): _description_
            next_page_link_string (str): _description_
        """
        
        self._first_page_request = self.InitializePageRequest(client, next_page_link_string)

    def InitializeLastPageRequest(self, client: ServiceNowClient, next_page_link_string: str) -> None:
        """Initializes the NextPageRequest property

        Args:
            client (_type_): _description_
            next_page_link_string (str): _description_
        """
        
        self._last_page_request = self.InitializePageRequest(client, next_page_link_string)

    def InitializePageRequest(self, client: ServiceNowClient, page_link_string: str) -> TableEntryCollectionRequest:
        if page_link_string == "" or page_link_string is None:
            return None

        return TableEntryCollectionRequest(ServiceNowEntry, page_link_string, client, None).Get

    @property
    def NextPageRequest(self) -> TableEntryCollectionRequest:
        return self._next_page_request

    def Append(self, entry: ServiceNowEntry) -> None:
        self._internal_list.append(entry)

    @classmethod
    def fromResponse(cls, response: Response, client: ServiceNowClient) -> 'ServiceNowTableEntriesCollectionPage':

        _new = cls()

        links = response.headers["Link"].split(",")

        next_link = None
        prev_link = None
        last_link = None
        first_link = None

        for link in links:
            if 'rel="first"' in link:
                first_link = link.split(";")[0]
            elif 'rel="next"' in link:
                next_link = link.split(";")[0]
            elif 'rel="prev"' in link:
                prev_link = link.split(";")[0]
            elif 'rel="last"' in link:
                last_link = link.split(";")[0]

        print(next_link, first_link, last_link, prev_link)

        _new.InitializeNextPageRequest(client, next_link)
        _new.InitializeFirstPageRequest(client, first_link)
        _new.InitializeLastPageRequest(client, last_link)
        _new.InitializePreviousPageRequest(client, prev_link)


        return _new