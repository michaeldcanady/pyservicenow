from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption

class BaseServiceNowRequest(BaseRequest):

    def __init__(self, request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(request_url, client, options)