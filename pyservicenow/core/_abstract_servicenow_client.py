from abc import ABC, abstractmethod
import typing
from pyrestwrapperbase import AbstractServiceClient
from logging import getLogger
from requests import Session, Response

# internal imports
from ..requests.builder._now_request_builder import NowRequestBuilder
from ..types.enums import APIVersion
from ._client_factory import HTTPClientFactory


class AbstractServiceNowClient(AbstractServiceClient, ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def Now(self, version: APIVersion=APIVersion.Null) -> NowRequestBuilder:
        raise NotImplementedError("'Now' method is not implemented")

    @abstractmethod
    def CustomEndpoint(self, endpoint: str) -> Response:
        raise NotImplementedError("'CustomEndpoint' method is not implemented")

    @property
    @abstractmethod
    def base_url(self) -> str:
        raise NotImplementedError("'base_url' getter method is not implemented")

    @base_url.setter
    @abstractmethod
    def base_url(self, value: str) -> str:
        raise NotImplementedError("'base_url' setter method is not implemented")

    @abstractmethod
    def _servicenow_url(self, url: str) -> str:
        raise NotImplementedError("'_servicenow_url' method is not implemented")