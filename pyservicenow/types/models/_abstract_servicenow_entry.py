"""Houses Service-Now Entry"""

from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar, Optional, Type, Union

from abc import abstractmethod

from datetime import datetime

from pyservicenow.types.models._abstract_servicenow_propery_collection import (
    AbstractServiceNowPropertyCollection,
)

from pyservicenow.types.models._servicenow_property_collection import (
    ServiceNowPropertyCollection,
)

from pyservicenow.types.models._servicenow_property import ServiceNowProperty

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

S = TypeVar("S", bound="AbstractServiceNowEntry")
C = TypeVar("C", bound="ServiceNowClient")
R = TypeVar("R")


class AbstractServiceNowEntry(AbstractServiceNowPropertyCollection):
    """Abstract Service-Now Entry Type"""

    @property
    @abstractmethod
    def sys_id(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

    @property
    @abstractmethod
    def sys_updated_on(self) -> datetime:
        """Gets the updated on date

        Returns:
            datetime: The updated on date
        """

    @property
    @abstractmethod
    def sys_updated_by(self) -> str:
        """Gets the last updater's username

        Returns:
            str: The last updater's username
        """

    @abstractmethod
    def update_object(self) -> bool:
        """updates the object in Service-Now

        Raises:
            NotImplementedError: _description_

        Returns:
            bool: If update is successful
        """

        raise NotImplementedError("Update is not implemented")

    @abstractmethod
    def get(
        self, key: str, _type: Optional[Type[R]] = None
    ) -> Union[R, datetime, str, None]:
        """Gets the value of the key and returns it as the included type

        Args:
            key (str): The key to get
            _type (Optional[Type[R]], optional): The type to return it as. Defaults to None.

        Raises:
            ValueError: _description_

        Returns:
            Union[R, datetime, None]: The ke as the expected type
        """
    
    @abstractmethod
    def _get_value(self, property: ServiceNowProperty, _type: Type[R]) -> Union[R, str, None]:
        """_summary_

        Args:
            property (ServiceNowProperty): _description_
            _type (Type[R]): _description_

        Returns:
            Union[R, str, None]: _description_
        """
    
    @abstractmethod
    def import_servicenow_property_collection(self: S, collection: ServiceNowPropertyCollection) -> S:
        """_summary_

        Args:
            self (S): _description_
            collection (ServiceNowPropertyCollection): _description_

        Returns:
            S: _description_
        """