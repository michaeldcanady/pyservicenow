"""Houses Service-Now Property Collection"""
from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterator,
    ItemsView,
    List,
    TypeVar,
    Type,
    Any,
    Union,
    KeysView,
)

from json import dumps
from pyrestsdk.type.model import Entity
from pyrestsdk.type.model._common_base import FrozenAttributes

from pyservicenow.types.models._servicenow_property import ServiceNowProperty

from pyservicenow.types.models._abstract_servicenow_propery_collection import (
    AbstractServiceNowPropertyCollection,
)

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

S = TypeVar("S", bound="ServiceNowPropertyCollection")
C = TypeVar("C", bound="ServiceNowClient")


class ServiceNowPropertyCollection(Entity, AbstractServiceNowPropertyCollection):
    """Service-Now Property Collection"""

    __metaclass__ = FrozenAttributes

    def __init__(self, client: C) -> None:
        super().__init__(client)

        self._is_null = True
        self._internaldict = {}
        self._changed_keys = []

    @property
    def is_null(self) -> bool:
        """Gets if the collection is null, contains no key/value pairs

        Returns:
            bool: If the collection is null
        """
        return self._is_null

    def _check_is_null(self) -> None:
        """checks if the object is empty"""
        self._is_null = len(self.keys()) == 0

    def __setitem__(
        self, key: str, value: Union[ServiceNowProperty, "ServiceNowPropertyCollection"]
    ) -> None:
        self._internaldict[key] = value
        self._check_is_null()
        if key not in self._changed_keys:
            self._changed_keys.append(key)

    def __getitem__(
        self, key: str
    ) -> Union[ServiceNowProperty, "ServiceNowPropertyCollection"]:
        return self._internaldict[key]

    def __len__(self) -> int:
        return len(self._internaldict)

    def __iter__(self) -> Iterator:
        return iter(self._internaldict)

    def __delitem__(self, key: str) -> None:
        del self._internaldict[key]
        self._check_is_null()

    def keys(self) -> List[str]:
        return list(self._internaldict.keys())

    def items(
        self,
    ) -> ItemsView[str, Union[ServiceNowProperty, "ServiceNowPropertyCollection"]]:
        return self._internaldict.items()

    def _changed_dict(self) -> Dict[str, Any]:
        changed_dict: Dict[str, Any] = {}

        for key in self._changed_keys:
            changed_dict[key] = self[key].actual_value

        return changed_dict

    @property
    def as_dict(self) -> Dict[str, Any]:
        _dict: Dict[str, Any] = {}

        for key, value in self._internaldict.items():
            
            _value = value
            
            if isinstance(value, ServiceNowProperty) or isinstance(value, ServiceNowPropertyCollection):
                _value = value.as_dict
            _dict[key] = _value

        return _dict

    @property
    def __json__(self) -> str:
        return dumps(self.as_dict)

    @property
    def as_json(self) -> Dict:
        """Gets the object as it's dict representation"""
        return self.as_dict

    def add_property(
        self, key, value: Union[Dict[str, Any], str, ServiceNowProperty]
    ) -> None:
        if isinstance(value, dict) or isinstance(value, str):
            value = ServiceNowProperty.__fromjson__(value)

        self[key] = value

    @classmethod
    def from_json(cls: Type[S], entry: Dict[str, Any], client: ServiceNowClient) -> S:
        new = cls(client)

        for key, value in entry.items():
            if "." in key:
                parent_key, child_key = key.split(".")

                if parent_key in new.keys():  # if it has the key
                    existing_value = new[parent_key]
                    if isinstance(existing_value, ServiceNowPropertyCollection):
                        existing_value.add_property(child_key, value)
                else:
                    value = ServiceNowPropertyCollection.from_json(
                        {child_key: value}, client
                    )
                    new[parent_key] = value
                continue

            new.add_property(key, value)

        new._check_is_null()
        new._changed_keys = []

        return new
