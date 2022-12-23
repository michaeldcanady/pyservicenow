from requests import Session
import typing
from logging import getLogger
from pyrestwrapperbase.middleware import AuthorizationHandler, BaseMiddleware

# internal imports
from ._username_password_credential import UsernamePasswordCredential
from .middleware.middleware import MiddlewarePipeline

Logger = getLogger(__name__)


class HTTPClientFactory:

    def __init__(self, api_url: str, session: Session):

        self.api_url = api_url
        Logger.debug(f"api url: {self.api_url}")
        self.session = session
        Logger.debug(f"session: {self.session}")

        self._set_base_url()
        # self._set_default_timeout()

    def create_with_default_middleware(self, credential: UsernamePasswordCredential, **kwargs) -> Session:
        """Applies the default middleware chain to the HTTP Client
        """
        middleware = [
            AuthorizationHandler(credential, **kwargs),
        ]
        self._register(middleware)
        return self.session

    def create_with_custom_middleware(self, *args, **kwargs) -> Session:
        raise NotImplementedError("create_with_custom_middleware is not implemented")

    def _set_base_url(self) -> None:
        """Helper method to set the base url"""
        self.session.base_url = f"https://{self.api_url}.service-now.com/api"

    def _register(self, middleware: typing.List[BaseMiddleware]) -> None:
        """
        Helper method that constructs a middleware_pipeline with the specified middleware
        """

        if middleware:
            middleware_pipeline = MiddlewarePipeline()
            for ware in middleware:
                middleware_pipeline.add_middleware(ware)

            self.session.mount('https://', middleware_pipeline)
