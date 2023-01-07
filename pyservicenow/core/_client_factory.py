"""Houses HTTPClientFactory"""

from logging import getLogger
from requests import Session
from pyrestsdk.middleware.authorizationhandler import BasicAuthorizationHandler
from pyrestsdk.clientfactory import AbstractHTTPClientFactory
from pyservicenow.core.credential._username_password_credential import (
    UsernamePasswordCredential,
)

Logger = getLogger(__name__)


class HTTPClientFactory(AbstractHTTPClientFactory):
    def __init__(self, api_url: str, session: Session) -> None:

        super().__init__(session=session)

        self.api_url = api_url
        Logger.debug(f"api url: {self.api_url}")

        self._set_base_url()
        # self._set_default_timeout()

    def create_with_default_middleware(
        self, credential: UsernamePasswordCredential, **kwargs
    ) -> Session:
        """Applies the default middleware chain to the HTTP Client"""

        Logger.info(f"{type(self)}.create_with_default_middleware(): method called")

        middleware = [
            BasicAuthorizationHandler(credential, **kwargs),
        ]
        self._register(middleware)
        return self.session

    def create_with_custom_middleware(self, *args, **kwargs) -> Session:
        """Applies custom middleware chain to the HTTP Client"""

        raise NotImplementedError("create_with_custom_middleware is not implemented")

    def _set_base_url(self) -> None:
        """Helper method to set the base url"""

        Logger.info(f"{type(self)}._set_base_url(): method called")

        # TODO subclass session or find new way to store base_url
        self.session.base_url = f"https://{self.api_url}.service-now.com/api"  # type: ignore

        Logger.debug(
            "%s._set_base_url() : base url set to: %s", type(self), self.session.base_url
        )
