from __future__ import annotations
from typing import TypeVar, TYPE_CHECKING, Iterable, Union, Optional, Dict, Callable
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

import json
from requests import Response
from logging import getLogger
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryRequest")

Logger = getLogger(__name__)

class TableEntryRequest(BaseTableRequest[S]):
    """The base Table Entry Request"""

    def __init__(
        self,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(request_url, client, options)

    @property
    def Invoke(self: B) -> S:
        
        _return = super().Invoke

        if type(_return) is not self.GenericType:
            raise UnexpectedReturnType(type(_return), self.GenericType)

        return _return
    
    def _sendRequest(self, value: Optional[S]) -> Optional[Response]:

        _request_dict: Dict[HttpsMethod, Callable] = {
            HttpsMethod.GET: self._client.get,
            HttpsMethod.POST: self._client.post,
            HttpsMethod.DELETE: self._client.delete,
            HttpsMethod.PUT: self._client.put,
        }

        Logger.info(
            f"{type(self).__name__}._sendRequest: {self.Method.name} request made"
        )

        _func = _request_dict.get(self.Method, None)

        if _func is None:
            raise Exception(f"Unknown HTTPS method {self.Method.name}")
        
        data = None
        
        if self.Method == HttpsMethod.PUT:
            data = value
        elif self.Method == HttpsMethod.PATCH or self.Method == HttpsMethod.POST:
            data = value.Json

        _response = _func(
            url=self.RequestUrl,
            params=str(self._query_options),
            data=json.dumps(data) if data is not None else None,
        )

        if self.Method == HttpsMethod.DELETE:
            return None

        return _response