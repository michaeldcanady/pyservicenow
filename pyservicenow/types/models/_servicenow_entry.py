from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from typing import overload, Optional, Dict, TypeVar, Type
from datetime import datetime
from abc import abstractmethod
# internal import
from ._servicenow_property_collection import ServiceNowPropertyCollection

S = TypeVar('S', bound='ServiceNowEntry')
C = TypeVar('C', bound='ServiceNowClient')


class ServiceNowEntry(ServiceNowPropertyCollection):
    
    __client: ServiceNowClient

    def __init__(self, client: ServiceNowClient) -> None:

        super().__init__(client)

    @property
    def Client(self) -> Optional[ServiceNowClient]:
        return self.__client

    @property
    def SysId(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

        return self["sys_id"].Value or self["sys_id"].DisplayValue

    @property
    def UpdatedOn(self) -> datetime:
        """Gets the updated on date

        Returns:
            datetime: The updated on date
        """

        raw_date = self["sys_updated_on"].Value

        return datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")

    @property
    def UpdatedBy(self) -> str:
        """Gets the last updater's username

        Returns:
            str: The last updater's username
        """

        return self["sys_updated_by"].Value

    @property
    def CreatedOn(self) -> datetime:
        """Gets the created on date

        Returns:
            datetime: The created on date
        """

        raw_date = self["sys_created_on"].Value

        return datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")

    def Update(self) -> bool:
        raise NotImplementedError("Update is not implemented")