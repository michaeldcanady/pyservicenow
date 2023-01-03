import json
import ssl
from typing import Optional, TypeVar
from requests import PreparedRequest, Response

from requests.adapters import HTTPAdapter
from urllib3 import PoolManager

from pyrestsdk.middleware import BaseMiddleware

# internal imports
from pyservicenow.core.middleware.request_context import RequestContext

B = TypeVar("B", bound=BaseMiddleware)

class MiddlewarePipeline(HTTPAdapter):
    """MiddlewarePipeline, entry point of middleware
    The pipeline is implemented as a linked-list, read more about
    it here https://buffered.dev/middleware-python-requests/
    """

    _current_middleware: Optional[B]
    _first_middleware: Optional[B]

    def __init__(self) -> None:
        super().__init__()
        self._current_middleware = None
        self._first_middleware = None
        self.poolmanager = PoolManager(ssl_version=ssl.PROTOCOL_TLSv1_2)

    def add_middleware(self, middleware: B) -> None:
        if self._current_middleware is not None:
            self._current_middleware.next = middleware
            self._current_middleware = middleware
        else:
            self._first_middleware = middleware
            self._current_middleware = self._first_middleware

    def send(self, request: PreparedRequest, **kwargs) -> Response:
        middleware_control_json = request.headers.pop('middleware_control', None)
        if middleware_control_json:
            middleware_control = json.loads(middleware_control_json)
        else:
            middleware_control = dict()
        
        # Set Context
        request.context = RequestContext(middleware_control, request.headers)

        if self._first_middleware is not None:
            return self._first_middleware.send(request, **kwargs)
        # No middleware in pipeline, call superclass' send
        return super().send(request, **kwargs)