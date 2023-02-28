"""Houses Service-Now Property Collection"""
from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    MutableMapping,
    Dict,
    Iterator,
    ItemsView,
    List,
    TypeVar,
    Type,
    Any,
    Union,
)
from abc import abstractmethod
from pyrestsdk.type.model._abstract_entity import AbstractEntity

from pyservicenow.types.models._servicenow_property import ServiceNowProperty

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

S = TypeVar("S", bound="AbstractServiceNowPropertyCollection")
C = TypeVar("C", bound="ServiceNowClient")


class AbstractServiceNowPropertyCollection(
    MutableMapping[str, Union[ServiceNowProperty, 'AbstractServiceNowPropertyCollection']], AbstractEntity
):

    _is_null: bool
    _internaldict: Dict[str, Union[ServiceNowProperty, 'AbstractServiceNowPropertyCollection']]
    _changed_keys: List[str]

    #@abstractmethod
    def __init__(self, client: ServiceNowClient) -> None:

        super().__init__(client)

    @property
    @abstractmethod
    def Client(self) -> ServiceNowClient:
        """Gets the client

        Args:
            self (S): AbstractServiceNowPropertyCollection

        Returns:
            C: The client
        """

    @property
    @abstractmethod
    def is_null(self) -> bool:
        """Gets if the collection is null, contains no key/value pairs

        Returns:
            bool: If the collection is null
        """

    @abstractmethod
    def _check_is_null(self) -> None:
        """checks if the object is empty"""

    @abstractmethod
    def __setitem__(self, key: str, value: Union[ServiceNowProperty, 'AbstractServiceNowPropertyCollection']) -> None:
        """Sets item at specificed key

        Args:
            key (str): Key to set
            value (ServiceNowProperty): Value to set to
        """

    @abstractmethod
    def __getitem__(self, key: str) -> Union[ServiceNowProperty, 'AbstractServiceNowPropertyCollection']:
        """Gets the value at specificed key

        Args:
            key (str): _description_

        Returns:
            ServiceNowProperty: _description_
        """

    @abstractmethod
    def __len__(self) -> int:
        """Gets count of properties

        Returns:
            int: Count of properties
        """

    @abstractmethod
    def __iter__(self) -> Iterator:
        """Gets properties as iterator

        Yields:
            Iterator: Properties as iterator
        """

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        """Deletes item at specified key

        Args:
            key (str): The key to remove
        """

    @abstractmethod
    def keys(self) -> List[str]:
        """Gets a list of the collection keys

        Returns:
            List[str]: list of the collection keys
        """

    @abstractmethod
    def items(self) -> ItemsView[str, ServiceNowProperty]:
        """Gets a set like collection of keys and values from the collection

        Returns:
            ItemsView[str, ServiceNowProperty]: Set like collection of keys and values
        """

    @abstractmethod
    def _changed_dict(self) -> Dict[str, Any]:
        """Gets a dictionary of the changed keys and their values

        Returns:
            Dict[str, Any]: Dictionary of the changed keys and their values
        """

    @property
    @abstractmethod
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object's dictionary representation

        Returns:
            Dict[str, Any]: The object's dictionary representation
        """

    @property
    @abstractmethod
    def __json__(self) -> str:
        """Gets the object as json

        Returns:
            str: The object as json
        """

    @property
    @abstractmethod
    def as_json(self) -> Dict[str, Any]:
        """Gets the object as json

        Returns:
            str: The object as json
        """

    @abstractmethod
    def add_property(self, key: str, value: Union[Dict[str, Any], str]) -> None:
        """Adds property to collection

        Args:
            key (str): Key to add
            value (Union[Dict[str, Any], str]): Value to add
        """

    @classmethod
    @abstractmethod
    def from_json(cls: Type[S], entry: Dict[str, Any], client: ServiceNowClient) -> S:
        """Converts entry from dictionary to new ServiceNowPropertyCollection.

        Args:
            entry (Dict): The entry to convert

        Returns:
            ServiceNowPropertyCollection: The Service-Now Property Collection
        """
