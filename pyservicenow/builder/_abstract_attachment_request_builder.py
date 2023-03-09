"""Houses abstract attachment request builder"""

from __future__ import annotations

from typing import Iterable, Optional, Union

from abc import abstractmethod

from pyrestsdk.requestbuilder._abstract_entity_request import (
    AbstractEntityRequestBuilder,
)

from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)

from pyservicenow.request import (
    AttachmentEntryRequest,
    AttachmentEntryCollectionRequest,
)


class AbstractAttachmentRequestBuilder(
    AbstractEntityRequestBuilder[AttachmentEntryCollectionRequest]
):
    """The Abstract Attachment Request Builder type"""

    @abstractmethod
    def request_with_options(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> AttachmentEntryCollectionRequest:
        """Constructs an Attachment Entry Collection Request

        Args:
            options (Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]):
            query or header options to include in the request

        Returns:
            AttachmentEntryCollectionRequest: The constructed Table Entry Collection Request
        """
    
    @property
    @abstractmethod
    def file(self):
        pass

    @abstractmethod
    def request_by_id(self, sys_id: str) -> AttachmentEntryRequest:
        """Constructs a Table Entry Request using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            AttachmentEntryRequest: The constructed Table Entry Request
        """
