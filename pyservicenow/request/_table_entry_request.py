from __future__ import annotations
import typing
from typing import TypeVar, Type, List, Optional, Generic, TYPE_CHECKING, Iterable, Union

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames
from pyservicenow.types.models import ServiceNowEntry, ServiceNowHeaderOption, ServiceNowQueryOption
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound='TableEntryRequest')


class TableEntryRequest(BaseTableRequest):
    """The base Table Entry Request
    """

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(_return_type, request_url, client, options)