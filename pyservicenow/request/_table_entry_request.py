from typing import Union, TypeVar, Type, List, Optional, Generic

# Interal Imports
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames
from pyservicenow.types.models import ServiceNowEntry, ServiceNowHeaderOption
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryRequest(BaseTableRequest):
    """The base Table Entry Request
    """

    def Get(self) -> ServiceNowEntry:
        """Gets a single Service-Now Entry

        Returns:
            ServiceNowEntry: The Service-Now Entry
        """

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.GET

        if (_return := self.Send(ServiceNowEntry, None)) is None:
            raise UnexpectedReturnType(type(_return), ServiceNowEntry)

        return _return

    def Delete(self) -> None:
        """Deletes a single Service-Now Entry
        """

        self.Method = HttpsMethods.DELETE

        if (_return := self.Send(ServiceNowEntry, None)) is not None:
            raise UnexpectedReturnType(type(_return), type(None))

        return _return

    def Send(self, obj_type: Type[S], object: Optional[S]) -> Optional[S]:

        if (type(_return := super().Send(obj_type, object)) is obj_type) or _return is None:
            return _return
        else:
            raise UnexpectedReturnType(type(_return), obj_type)