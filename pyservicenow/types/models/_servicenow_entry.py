from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import _servicenow_client

from typing import overload, Optional, Dict, TypeVar, Type
from datetime import datetime
from abc import abstractmethod
# internal import
from ._servicenow_property_collection import ServiceNowPropertyCollection

S = TypeVar('S', bound='ServiceNowEntry')
C = TypeVar('C', bound='_servicenow_client.ServiceNowClient')


class ServiceNowEntry(ServiceNowPropertyCollection):

    __client: Optional[_servicenow_client.ServiceNowClient] = None

    def __init__(self, _value: ServiceNowPropertyCollection = ServiceNowPropertyCollection(), client: Optional[_servicenow_client.ServiceNowClient] = None) -> None:

        super().__init__()

    @property
    def Client(self) -> Optional[_servicenow_client.ServiceNowClient]:
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