from __future__ import annotations
from typing import TYPE_CHECKING, Dict, TypeVar, Callable, List, Union, Type, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

import logging
from urllib.parse import urlparse
import json
import typing


# Internal Imports
from pyservicenow.types.enums import HttpsMethods
from pyservicenow.types.models._base_entity import BaseEntity

Logger = logging.getLogger(__name__)

S = TypeVar("S", bound='ServiceNowClient')

T = TypeVar("T", bound='BaseEntity')


class BaseRequest:

    _content_type: str
    _headers = {}
    _method: HttpsMethods
    _request_url: str
    _query_options = {}
    _client: 'ServiceNowClient'

    def __init__(self, request_url: str, client: 'ServiceNowClient', options) -> None:

        self._method = HttpsMethods.GET
        self._client = client
        # self._response_handler
        # self._middleware
        self._request_url = self._initializeUrl(request_url)

    @property
    def ContentType(self) -> str:
        return self._content_type

    @ContentType.setter
    def ContentType(self, value: str) -> None:
        self._content_type = value

    @property
    def Headers(self) -> typing.Dict:
        return self._headers

    @property
    def Client(self):
        return self._client

    @property
    def Method(self):
        return self._method

    @Method.setter
    def Method(self, value) -> None:
        self._method = value
        Logger.info(f"{type(self).__name__}.Method: _method set to {value}")

    @property
    def RequestUrl(self) -> str:
        return self._request_url

    @RequestUrl.setter
    def RequestUrl(self, value: str) -> None:
        self._request_url = value
        Logger.info(
            f"{type(self).__name__}.RequestUrl: _request_url set to {value}")

    @property
    def QueryOptions(self) -> typing.Dict:
        return self._query_options

    def _initializeUrl(self, request_url: str):
        if not request_url:
            pass

        uri = urlparse(request_url)

        if uri.query:
            queryString = uri.query
            if queryString[0] == '?':
                queryString == queryString[1:]

            # https://github.com/microsoftgraph/msgraph-sdk-dotnet-core/blob/4669ead37a66fabda43d1f0e20a02e1e69652946/src/Microsoft.Graph.Core/Requests/BaseRequest.cs#L430
            # QueryOptions = queryString.split('&')
            # Make get query options

        return request_url

    def AppendSegmentToRequestUrl(self, url_segment: str) -> None:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.
        """

        self._request_url = "{0}/{1}".format(self.RequestUrl, url_segment)

    def Send(self, obj_type: Type[T], object, cancellation_token, http_completion_option=None) -> Optional[Union[List[T], T]]:

        Logger.info(f"{type(self).__name__}.Send: method called")

        return self.SendRequest(obj_type, object, http_completion_option)

    def SendRequest(self, obj_type: Type[T], value: Optional[T], HttpCompletionOption=None) -> Optional[Union[List[T], T]]:

        _response = self._sendRequest(value)

        if _response is None:
            return None

        result = _response["result"]

        _type_return = {
            dict: parse_result,
            list: parse_result_list
        }

        _func = _type_return.get(type(result), None)

        if _func is None:
            raise Exception(f"Unexcepted result type: {type(result)}")

        return _func(obj_type, result, self.Client)

    def _sendRequest(self, value: Optional[T]) -> Optional[Dict[str, Union[List, Dict]]]:

        _request_dict: Dict[HttpsMethods, Callable] = {
            HttpsMethods.GET: self._client.get,
            HttpsMethods.POST: self._client.post,
            HttpsMethods.DELETE: self._client.delete,
            HttpsMethods.PUT: self._client.put
        }

        Logger.info(
            f"{type(self).__name__}.SendRequest: {self.Method.name} request made")

        _func = _request_dict.get(self.Method, None)

        if _func is None:
            raise Exception(f"Unknown HTTPS method {self.Method.name}")

        _response = _func(
            url=self.RequestUrl,
            params=self._query_options,
            data=json.dumps(value.Json()) if value is not None else None
        )

        if (self.Method == HttpsMethods.DELETE):
            return None

        return _response.json()


def parse_result(obj_type: Type[T], result: Dict, client) -> T:
    return obj_type().fromJson(result)


def parse_result_list(obj_type: Type[T], results: List, client) -> List[T]:
    _results: List[T] = []

    for raw_result in results:
        _entry = obj_type().fromJson(raw_result)
        _entry.__client = client
        _results.append(_entry)

    return _results
