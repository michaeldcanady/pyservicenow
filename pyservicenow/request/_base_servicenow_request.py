"""Houses Base Service-Now Entry Request"""

from __future__ import annotations
import json
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

from logging import getLogger
from requests import Response

from pyrestsdk.request.supports_types import SupportsGetMethod, SupportsPostMethod
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
S = TypeVar("S", bound=ServiceNowEntry)

Logger = getLogger(__name__)


class BaseServiceNowEntryRequest(SupportsGetMethod, BaseRequest[S]):
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
        
        self.header_options.append(
            ServiceNowHeaderOption(Header.ACCEPT, MimeTypeName.Application.JSON)
        )

        self._object = None

    def parse_response(
        self: B, _response: Optional[Response]
    ) -> Optional[Union[List[S], S]]:
        """Parses response into expected return type, list of generic type,
        single generic type or None"""

        if _response is None:
            return None

        _json_text = _response.text
        _json = json.loads(_json_text)    
    
        try:
            _response.raise_for_status()
        except Exception as e:
            self.parse_exception(_json)
        else:
            _result = _json["result"]

        return parse_result(self._generic_type, _result, self.Client)
    
    def parse_exception(self, json: Dict[str, Any]):
        raise Exception("ERROR")
    
def parse_result(
    obj_type: S,
    result: Union[Dict[str, Any], List[Dict[str, Any]]],
    client
) -> Union[List[S], S]:
    """parses return into expected return type"""

    _operation_dict: Dict[
        Type, Callable[[Union[Dict, List], ServiceNowClient], Union[List[S], S]]
    ] = {
        dict: lambda x, y: obj_type.from_json(x, y),  # type: ignore
        list: lambda x, y: [
            obj_type.from_json(raw_result, y) for raw_result in x
        ],
    }

    if (_func := _operation_dict.get(type(result), None)) is None:
        raise Exception(f"unexpected type: {type(result)}")

    return _func(result, client)
