"""Houses Service-Now Entry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Optional, Type, Union

from datetime import datetime

from pyservicenow.types.models._abstract_servicenow_entry import AbstractServiceNowEntry

from pyservicenow.types.models._servicenow_property_collection import (
    ServiceNowPropertyCollection,
)

from pyservicenow.types.models._servicenow_property import ServiceNowProperty

from pyservicenow.types.constants import DATETIME, DATE

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

S = TypeVar("S", bound="ServiceNowEntry")
C = TypeVar("C", bound="ServiceNowClient")
R = TypeVar("R")


class ServiceNowEntry(ServiceNowPropertyCollection, AbstractServiceNowEntry):
    """Service-Now Entry Type"""
    
    def __init__(self, client) -> None:
        super().__init__(client)

    @property
    def sys_id(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

        return self._get_output("sys_id")

    @property
    def sys_updated_on(self) -> datetime:
        """Gets the updated on date

        Returns:
            datetime: The updated on date
        """

        return self.get("sys_updated_on", datetime)

    @property
    def sys_updated_by(self) -> str:
        """Gets the last updater's username

        Returns:
            str: The last updater's username
        """

        return self["sys_updated_by"].actual_value

    @property
    def sys_created_on(self) -> datetime:
        """Gets the created on date

        Returns:
            datetime: The created on date
        """

        return self.get("sys_created_on", datetime)

    def update_object(self) -> bool:
        """updates the object in Service-Now"""
        raise NotImplementedError("Update is not implemented")

    def _get_output(self, key: str) -> Any:
        """Gets the actual or display value based on which has a valid value"""

        _value = self[key]

        return _value.actual_value or _value.display_value

    def get(self, key: str, _type: Optional[Type[R]] = None) -> Union[R, datetime, str, None]:
        
        #TODO Add support for sys_id checking
        
        if _type is None:
            _type = ServiceNowEntry
        
        raw_value = self[key]
        
        if isinstance(raw_value, ServiceNowProperty) and _type == datetime:
            return self.parse_servicenow_datetime(raw_value.actual_value)
        
        if issubclass(_type, ServiceNowPropertyCollection):
            return _type(self.Client).import_servicenow_property_collection(raw_value)
        
        if isinstance(raw_value, ServiceNowProperty):
            return self._get_value(raw_value, _type)
        
        raise ValueError(f"value: {raw_value} of type: {type(raw_value)} is unexpected")
    
    def _get_value(self, property: ServiceNowProperty, _type: Type[R]) -> Union[R, str, None]:
        
        if property.display_value != "" and property.display_value is not None:
            return _type(property.display_value)
        elif property.display_value == "" or property.display_value is None:
            return None

        return _type(property.actual_value)
    
    def import_servicenow_property_collection(self: S, collection: ServiceNowPropertyCollection) -> S:
        
        for key, value in collection.items():
            self[key] = value
        
        return self
        
    @staticmethod    
    def parse_servicenow_datetime(timestamp: str) -> datetime:
        
        try:
            return datetime.strptime(timestamp, DATETIME)
        except:
            return datetime.strptime(timestamp, DATE)