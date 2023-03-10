from typing import Optional, Iterable, Union

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)
from pyservicenow.request import AttachmentFileEntryRequest

class AttachmentFileRequestBuilder(EntityRequestBuilder):
    
    def __init__(self, request_url: str, client) -> None:
        super().__init__(request_url, client)
    
    @property
    def request(self) -> AttachmentFileEntryRequest:
        return self.request_with_options(None)
    
    def request_with_options(self, options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]) -> AttachmentFileEntryRequest:
        return AttachmentFileEntryRequest(self.request_url, self.request_client, options)