from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
    ServiceNowEntry,
)
from pyservicenow.types.enums import Header, MimeTypeNames

B = TypeVar("B", bound="BaseServiceNowEntryRequest")
S = TypeVar("S", bound="ServiceNowEntry")


class BaseServiceNowEntryRequest(BaseRequest):
    def __init__(
        self,
        _return_type: Type[S],
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(_return_type, request_url, client, options)

        self._object: Optional[S] = None

    @property
    def Get(self: B) -> B:
        """Sets request to get request"""

        self._headers.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )
        self.Method = HttpsMethod.GET
        self._object = None

        return self

    def Post(self: B, input_object: S) -> B:

        self._headers.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )
        self.Method = HttpsMethod.POST
        self._object = input_object

        return self

    def Delete(self: B) -> B:

        self._headers.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )
        self.Method = HttpsMethod.DELETE
        self._object = None

        return self

    def Put(self: B, input_object: S) -> B:

        self._headers.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )
        self.Method = HttpsMethod.PUT
        self._object = input_object

        return self

    @property
    def Invoke(self: B) -> S:

        return self.Send(self._object)
