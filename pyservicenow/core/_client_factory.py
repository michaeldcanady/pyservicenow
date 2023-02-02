"""Houses HTTPClientFactory"""

from logging import getLogger

from typing import List, TypeVar

from requests import Session

from pyrestsdk.middleware.authorizationhandler import BasicAuthorizationHandler
from pyrestsdk.middleware import MiddlewarePipeline, BaseMiddleware
from pyrestsdk.clientfactory import AbstractHTTPClientFactory
from pyrestsdk.credential import BasicCredential

B = TypeVar("B", bound=BaseMiddleware)

Logger = getLogger(__name__)


class HTTPClientFactory(AbstractHTTPClientFactory):
    """HTTP Client Factory type"""

    def __init__(self, api_url: str, session: Session) -> None:

        super().__init__(session=session)

        self.api_url = api_url
        Logger.debug("api url: %s", self.api_url)

        self._set_base_url(api_url)
        # self._set_default_timeout()

    def create_with_default_middleware(
        self, credential: BasicCredential, **kwargs
    ) -> Session:
        """Applies the default middleware chain to the HTTP Client"""

        Logger.info(
            "%s.create_with_default_middleware(): method called", type(self).__name__
        )

        middleware = [
            BasicAuthorizationHandler(credential, **kwargs),
        ]
        self._register(middleware)
        return self.session

    def create_with_custom_middleware(self, *args, **kwargs) -> Session:
        """Applies custom middleware chain to the HTTP Client"""

        raise NotImplementedError("create_with_custom_middleware is not implemented")

    def _set_base_url(self, url: str) -> None:
        """Helper method to set the base url"""

        Logger.info("%s._set_base_url(): method called", type(self).__name__)

        # TODO subclass session or find new way to store base_url
        self.session.base_url = f"https://{url}.service-now.com/api"  # type: ignore

        Logger.debug(
            "%s._set_base_url() : base url set to: %s",
            type(self),
            self.session.base_url,
        )

    def _register(self, middleware: List[B]) -> None:
        """
        Helper method that constructs a middleware_pipeline with the specified middleware
        """

        Logger.info("%s._register: method called", type(self))

        if middleware:
            middleware_pipeline = MiddlewarePipeline()
            for ware in middleware:
                middleware_pipeline.add_middleware(ware)

            self.session.mount("https://", middleware_pipeline)
