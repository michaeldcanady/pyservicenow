"""Houses Service-Now Client"""

import typing
from logging import getLogger
from requests import Session, Response
from pyrestsdk import AbstractServiceClient
from pyservicenow.builder._now_request_builder import NowRequestBuilder
from pyservicenow.types.enums import APIVersion
from pyservicenow.core._client_factory import HTTPClientFactory

Logger = getLogger(__name__)


class ServiceNowClient(AbstractServiceClient):
    """Service-Now Client type"""

    @typing.overload
    def __init__(self, credential, instance: str, session: Session = Session()) -> None:
        ...

    @typing.overload
    def __init__(self, middleware, instance: str, session: Session = Session()) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        Logger.info("getting LUEDMAPI session")

        instance = kwargs.pop("instance", None)
        session = kwargs.pop("session", Session())

        if instance is None:
            raise Exception("instance is required")

        self.lu_edm_api_session: Session = self._get_session(
            instance, session, **kwargs
        )

    @property
    def Now(self) -> NowRequestBuilder:
        """Constructs Now Request Builder"""

        return NowRequestBuilder(f"{self.base_url}/now", self)

    @property
    def base_url(self) -> str:
        """Gets/Sets the request's base URL"""
        return self.lu_edm_api_session.base_url  # type: ignore

    @base_url.setter
    def base_url(self, base: str) -> None:
        self.lu_edm_api_session.base_url = base  # type: ignore

    def custom_endpoint(self, endpoint: str) -> Response:
        """Construct request to non-standard endpoint"""
        return self.get(endpoint)

    def get(self, url: str, **kwargs) -> Response:
        r"""Sends a GET request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.get: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)

        return self.lu_edm_api_session.get(self._instance_url(url), **kwargs)

    def options(self, url: str, **kwargs) -> Response:
        r"""Sends a OPTIONS request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.options: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)

        return self.lu_edm_api_session.options(self._instance_url(url), **kwargs)

    def head(self, url: str, **kwargs) -> Response:
        r"""Sends a HEAD request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.head: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)

        return self.lu_edm_api_session.head(self._instance_url(url), **kwargs)

    def post(self, url: str, data=None, json=None, **kwargs) -> Response:
        r"""Sends a POST request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.post: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)
        Logger.debug("data: %s", data)
        Logger.debug("json: %s", json)

        return self.lu_edm_api_session.post(
            self._instance_url(url), data=data, json=json, **kwargs
        )

    def put(self, url: str, data=None, **kwargs) -> Response:
        r"""Sends a PUT request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.lu_edm_api_session.put(self._instance_url(url), data=data, **kwargs)

    def patch(self, url: str, data=None, **kwargs) -> Response:
        r"""Sends a PATCH request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.patch: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)
        Logger.debug("data: %s", data)

        return self.lu_edm_api_session.patch(
            self._instance_url(url), data=data, **kwargs
        )

    def delete(self, url: str, **kwargs) -> Response:
        r"""Sends a DELETE request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        Logger.info("%s.delete: function called", type(self).__name__)
        Logger.debug("url: %s", self._instance_url(url))
        Logger.debug("kwargs: %s", kwargs)

        return self.lu_edm_api_session.delete(self._instance_url(url), **kwargs)

    def _instance_url(self, url: str) -> str:
        """Appends BASE_URL to user provided path
        :param url: user provided path
        :return: graph_url
        """
        _url = self.base_url + url if (url[0] == "/") else url

        Logger.info("%s._servicenow_url: function called", type(self).__name__)
        Logger.debug("url: %s", _url)

        return _url

    @staticmethod
    def _get_session(instance: str, session: Session, **kwargs) -> Session:
        """Method to always retrun a single instance of an HTTP Client"""

        Logger.info("LUEDMServiceClient._get_luedmapi_session: function called")

        credential = kwargs.pop("credential", None)

        Logger.debug("credential: %s", credential)

        middleware = kwargs.pop("middleware", None)

        Logger.debug("middleware: %s", middleware)

        if credential and middleware:
            raise ValueError(
                "Invalid parameters! Both TokenCredential and middleware cannot be passed"
            )
        if not credential and not middleware:
            raise ValueError(
                "Invalid parameters!. Missing TokenCredential or middleware"
            )

        if credential is not None:
            Logger.debug("Creating with default middleware")
            return HTTPClientFactory(instance, session).create_with_default_middleware(
                credential, **kwargs
            )
        return HTTPClientFactory(instance, session).create_with_custom_middleware(
            middleware
        )
