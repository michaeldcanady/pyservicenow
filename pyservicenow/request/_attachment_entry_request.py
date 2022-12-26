from __future__ import annotations
import typing
from typing import Union, TypeVar, Iterable, List, Optional, Generic, TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.types.enums import QueryParameters, DisplayValue, View
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models.querybuilder import QueryBuilder
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption

T = TypeVar("T", bound='BaseAttachmentRequest')

class AttachmentEntryRequest(BaseAttachmentRequest):

    def __init__(self, request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(request_url, client, options)

    def Get(self):
        pass