from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames
from pyservicenow.types.models import ServiceNowHeaderOption

B = TypeVar("B", bound='BaseServiceNowRequest')

class BaseServiceNowRequest(BaseRequest):

    def __init__(self, request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(request_url, client, options)

    def Get(self: B) -> B:
        
        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.GET

        return self