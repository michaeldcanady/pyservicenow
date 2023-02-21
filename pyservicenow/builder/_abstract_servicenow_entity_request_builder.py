"""Houses Abstract Service-Now Entity Request Builder"""
from typing import TypeVar

from abc import abstractmethod

from pyrestsdk.requestbuilder._abstract_entity_request import (
    AbstractEntityRequestBuilder,
)

from pyservicenow.request import BaseServiceNowEntryRequest

A = TypeVar("A", bound="AbstractServiceNowEntityRequestBuilder")
B = TypeVar("B", bound=BaseServiceNowEntryRequest)


class AbstractServiceNowEntityRequestBuilder(AbstractEntityRequestBuilder):
    """Abstract Service-Now Entity Request Builder Type"""
    
    @abstractmethod
    def request_by_id(self, sys_id: str) -> B:
        """Constructs a Entry Request using the provided sys_id

        Args:
            sys_id (str): Entry's sys_id

        Returns:
            BaseServiceNowEntryRequest: The constructed Entry Request
        """
