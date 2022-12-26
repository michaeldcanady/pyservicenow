from __future__ import annotations
import typing
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# internal imports
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry

class AttachmentEntry(ServiceNowEntry):

    def __init__(self, _value: ServiceNowEntry = ServiceNowEntry(), client: Optional[ServiceNowClient] = None) -> None:
        super().__init__(_value, client)

    @property
    def ContentType(self):
        raise NotImplementedError("ContentType is not implemented")

    @property
    def FileName(self) -> str:
        raise NotImplementedError("FileName is not implemented")

    @property
    def Width(self):
        raise NotImplementedError("Width is not implemented")

    @property
    def Height(self):
        raise NotImplementedError("Height is not implemented")

    @property
    def TableName(self) -> str:
        raise NotImplementedError("TableName is not implemented")

    @property
    def DownloadLink(self) -> str:
        raise NotImplementedError("DownloadLink is not implemented")

    @property
    def AverageImageColor(self):
        raise NotImplementedError("AverageImageColor is not implemented")
    
    @property
    def Size(self):
        raise NotImplementedError("Size is not implemented")

    @property
    def CompressedSize(self):
        raise NotImplementedError("CompressedSize is not implemented")

    @property
    def TableSysId(self) -> str:
        raise NotImplementedError("TableSysId is not implemented")

    @property
    def IsCompressed(self) -> bool:
        raise NotImplementedError("IsCompressed is not implemented")