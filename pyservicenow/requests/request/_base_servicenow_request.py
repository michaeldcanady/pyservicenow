from __future__ import annotations
import typing
from typing import Union, TypeVar, Type, List, Optional, Generic, TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.requests.request._base_request import BaseRequest

class BaseServiceNowRequest(BaseRequest):

    def __init__(self, request_url: str, client: 'ServiceNowClient', options) -> None:
        super().__init__(request_url, client, options)