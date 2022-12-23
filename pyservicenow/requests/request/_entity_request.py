from abc import abstractmethod

# internal imports
from ._base_request import BaseRequest
from pyservicenow.types.enums import MimeTypeNames
from pyservicenow.types.enums import HttpsMethods
from pyservicenow.types.models._entity import Entity

class EntityRequest(BaseRequest):
    
    def __init__(self, request_url: str, client, options) -> None:
        super().__init__(request_url, client, options)
        
    def Create(self, entity_to_create: Entity, cancellation_token) -> Entity:
        """Creates the specified Entity using POST.

        Args:
            entity_to_create (Entity): The Entity to create.
            cancellation_token (): The System.Threading.CancellationToken for the request.

        Returns:
            Entity:  The created Entity.
        """
        
        self.ContentType = MimeTypeNames.Application.JSON
        self.Method = HttpsMethods.POST
        
        entity: Entity = self.Send(entity_to_create, cancellation_token)
        
        self.InitializeCollectionProperties(entity)
        
        return entity
    
    @abstractmethod
    def InitializeCollectionProperties(entity_to_initialize: Entity):...