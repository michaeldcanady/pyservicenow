from __future__ import annotations
from typing import TYPE_CHECKING, MutableMapping, Dict, Iterator, ItemsView, List, TypeVar, Type
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.type.model import BaseEntity

from pyrestsdk.type.model import BaseEntity

# internal imports
from ._servicenow_property import ServiceNowProperty

S = TypeVar('S', bound='ServiceNowPropertyCollection')

class ServiceNowPropertyCollection(MutableMapping[str, ServiceNowProperty], BaseEntity):

    is_null: bool = True
    _internaldict: Dict[str, ServiceNowProperty] = dict()
    _changed_keys: List[str] = []

    def __init__(self, client: ServiceNowClient) -> None:
        super().__init__(client)
    def __init__(self, client: ServiceNowClient) -> None:
        super().__init__(client)

    @property
    def IsNull(self) -> bool:
        """Gets if the collection is null, contains no key/value pairs

        Returns:
            bool: If the collection is null
        """

        return self.is_null

    def _check_is_null(self) -> None:
        self.is_null = (len(self.keys()) == 0)
    
    def __setitem__(self, key: str, value: ServiceNowProperty) -> None:

        self._internaldict[key] = value
        self._check_is_null()
        if key not in self._changed_keys:
            self._changed_keys.append(key)

    def __getitem__(self, key: str) -> ServiceNowProperty:
        return self._internaldict[key]

    def __len__(self) -> int:
        return len(self._internaldict)
    
    def __iter__(self) -> Iterator:
        return iter(self._internaldict)

    def __delitem__(self, key: str) -> None:
        del self._internaldict[key]
        self._check_is_null()
    
    def keys(self):
        """Gets a list of the collection keys

        Returns:
            _type_: _description_
        """

        return self._internaldict.keys()
    
    def items(self) -> ItemsView[str, ServiceNowProperty]:
        """Gets a set like collection of keys and values from the collection

        Returns:
            ItemsView[str, ServiceNowProperty]: Set like collection of keys and values
        """

        return self._internaldict.items()

    @classmethod
    def fromJson(cls: Type[S], entry: Dict, client: ServiceNowClient) -> S:
    def fromJson(cls: Type[S], entry: Dict, client: ServiceNowClient) -> S:
        """Converts entry from dictionary to new ServiceNowPropertyCollection.

        Args:
            entry (Dict): The entry to convert

        Returns:
            ServiceNowPropertyCollection: The Service-Now Property Collection
        """

        new = cls(client)
        new = cls(client)

        for key, value in entry.items():
            _value = ServiceNowProperty()
            if isinstance(value, str):
                _value.Value = value
            else:
                if value is not None:
                    _value.DisplayValue = value.get("display_value")
                    _value.Value = value.get("value")
                    _value.Link = value.get("link")

            new[key] = _value

        new._changed_keys = []
        
        return new