from __future__ import annotations
from typing import Generic, TypeVar, List, Type,TYPE_CHECKING, Optional, Dict, get_args
if TYPE_CHECKING:
    from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
    from pyservicenow.core import ServiceNowClient
from requests import Response
from abc import abstractmethod
# internal imports
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry
from pyservicenow.types.models._accessible_generic import AccessibleGeneric

T = TypeVar("T", bound=ServiceNowEntry)
C = TypeVar("C", bound='CollectionPage')

class CollectionPage(AccessibleGeneric[T]):

    _internal_list: List[T]
    _next_request: Optional[BaseServiceNowEntryRequest] = None

    def __init__(self, client: ServiceNowClient) -> None:
        super().__init__()
        
        self._internal_list = []
        self._next_request = None

    @property
    def CurrentPage(self) -> List[T]:
        return self._internal_list

    @classmethod
    @abstractmethod
    def fromResponse(cls: Type[C], response: Response) -> C: ...
    
    @classmethod
    def fromJson(cls: Type[C], entries: List[Dict], client: ServiceNowClient) -> C:
        
        _new = cls(client)
        
        _type: Type[T] = _new.GenericType
        
        _new._internal_list = [_type.fromJson(entry, client) for entry in entries]
        
        return _new