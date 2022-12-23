import typing

# internal imports
from ._base_request_builder import BaseRequestBuilder
from pyservicenow.requests.request import EntityRequest

class EntityRequestBuilder(BaseRequestBuilder):
    """The type EntityRequestBuilder.
    """
    

    def __init__(self, request_url: str, client) -> None:
        """Constructs a new EntityRequestBuilder.

        Args:
            request_url (str): The URL for the built request.
            client (_type_): The BaseClient for handling requests.
        """
        
        super().__init__(request_url, client)
    
    @property
    def Request(self) -> EntityRequest:
        """Builds the request.

        Returns:
            EntityRequest: The built request.
        """
        return EntityRequest(self.RequestUrl, self.Client, None)