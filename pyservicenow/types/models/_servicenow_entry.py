"""Houses Service-Now Entry"""

from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar
from datetime import datetime
from pyservicenow.types.models._servicenow_property_collection import ServiceNowPropertyCollection
from pyservicenow.types.constants import DATETIME

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

S = TypeVar("S", bound="ServiceNowEntry")
C = TypeVar("C", bound="ServiceNowClient")


class ServiceNowEntry(ServiceNowPropertyCollection):
    """Service-Now Entry Type"""

    @property
    def user_sys_id(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

        return self["sys_id"].actual_value or self["sys_id"].display_value

    @property
    def sys_updated_on(self) -> datetime:
        """Gets the updated on date

        Returns:
            datetime: The updated on date
        """

        raw_date = self["sys_updated_on"].actual_value

        return datetime.strptime(raw_date, DATETIME)

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

        raw_date = self["sys_created_on"].actual_value

        return datetime.strptime(raw_date, DATETIME)

    def Update(self) -> bool:
        """updates the object in Service-Now"""
        raise NotImplementedError("Update is not implemented")
