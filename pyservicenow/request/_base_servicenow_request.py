from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Iterable,
    Union,
    TypeVar,
    Type,
    Optional,
    List,
    Dict,
    Any,
    Callable,
)

import json

from logging import getLogger
from requests import Response
from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
    ServiceNowEntry,
)
from pyservicenow.types.enums import Header, MimeTypeName

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

B = TypeVar("B", bound="BaseServiceNowEntryRequest")
S = TypeVar("S", bound="ServiceNowEntry")

Logger = getLogger(__name__)


class BaseServiceNowEntryRequest(BaseRequest[S]):
    """Base Service-Now Entry Request"""
    
    def __init__(
        self,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(request_url, client, options)

        self._object = None

    @property
    def Object(self: B) -> Optional[S]:
        """Gets/Sets object"""

        return self._object

    @Object.setter
    def Object(self: B, value: Optional[S]) -> None:
        Logger.info(f"{type(self).__name__}.Object: function called")

        self._object = value

        Logger.info(f"{type(self).__name__}.Object: object changed")

    @property
    def Get(self: B) -> B:
        """Sets request to get request"""

        self.header_options.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )

        self._update_request_type(HttpsMethod.GET, None)

        return self

    def Post(self: B, input_object: S) -> B:

        self.header_options.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )

        self._update_request_type(HttpsMethod.POST, input_object)

        return self

    @property
    def Delete(self: B) -> B:
        """Sets request to delete request"""

        self.header_options.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )

        self._update_request_type(HttpsMethod.DELETE, None)

        return self

    def Put(self: B, input_object: S) -> B:
        """Sets request to put request"""

        self.header_options.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )

        self._update_request_type(HttpsMethod.PUT, input_object)

        return self

    def _update_request_type(
        self: B, method: HttpsMethod, input_object: Optional[S]
    ) -> None:
        """Updates the request type, sSets the method and object to the provided values"""

        Logger.info(f"{type(self).__name__}._update_request_type: function called")

        self.Method = method
        self.Object = input_object

    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[S], S]]:
        """Parses response into expected return type, list of generic type,
        single generic type or None"""

        if _response is None:
            return None

        _json_text = _response.text
        _json = json.loads(_json_text)
        _result = _json["result"]

        return parse_result(self.generic_type, _result, self.Client)

    @property
    def Invoke(self: B) -> Optional[Union[List[S], S]]:
        """Invokes the specified method"""

        return self.Send(self._object)


def parse_result(
    obj_type: Type[S],
    result: Union[Dict[str, Any], List[Dict[str, Any]]],
    client: ServiceNowClient,
) -> Union[List[S], S]:

    _operation_dict: Dict[
        Type, Callable[[Union[Dict, List], ServiceNowClient], Union[List[S], S]]
    ] = {
        dict: lambda x, y: obj_type.fromJson(x, y),  # type: ignore
        list: lambda x, y: [obj_type.fromJson(raw_result, y) for raw_result in x],
    }

    if (_func := _operation_dict.get(type(result), None)) is None:
        raise Exception(f"unexpected type: {type(result)}")

    return _func(result, client)
