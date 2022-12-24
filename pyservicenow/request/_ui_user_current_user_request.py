from typing import Union, TypeVar, Type, List, Optional, Generic

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.enums import HttpsMethods
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

T = TypeVar("T", bound=BaseRequest)
S = TypeVar("S", bound=ServiceNowEntry)


class UIUserCurrentUserRequest(BaseRequest):
    """The Table Entry Collection Request
    """

    def Get(self) -> 'CurrentUser':
        """Gets a single Service-Now Entry

        Returns:
            ServiceNowEntry: The Service-Now Entry
        """


        # MimeTypeNames.Application.JSON
        self._headers["Accept"] = "application/json"
        self.Method = HttpsMethods.GET

        return self.Send(CurrentUser, None)

    def Send(self, obj_type: Type[S], object: Optional[S]) -> S:


        if type(_return := super().Send(obj_type, object, None, None)) is not obj_type:
            raise UnexpectedReturnType(type(_return), obj_type)
        
        return _return

from pyservicenow.types.models import CurrentUser