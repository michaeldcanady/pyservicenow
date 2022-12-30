from __future__ import annotations
from typing import Generic, TypeVar, List, Type,TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from requests import Response
from abc import abstractmethod
# internal imports
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry

T = TypeVar("T", bound=ServiceNowEntry)
C = TypeVar("C", bound='CollectionPage')

class CollectionPage(Generic[T]):

    _internal_list: List[T]
    _next_request: BaseServiceNowEntryRequest = None

    def __init__(self) -> None:
        super().__init__()

    @property
    def CurrentPage(self) -> List[T]:
        return self._internal_list

    @classmethod
    @abstractmethod
    def fromResponse(cls: Type[C], response: Response) -> C: ...