from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from os.path import exists, join

# internal imports
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry
from pyservicenow.types.enums import EncryptionContext

class AttachmentEntry(ServiceNowEntry):

    def __init__(self, client: ServiceNowClient) -> None:
        super().__init__(client)

    @property
    def ContentType(self):
        return self["content_type"].Value

    @property
    def FileName(self) -> str:
        return self["file_name"].Value
    
    @property
    def Tags(self):
        return self["sys_tags"].Value

    @property
    def TableName(self) -> str:
        return self["table_name"].Value

    @property
    def DownloadLink(self) -> str:
        return self["download_link"].Value
    
    def Download(self, download_path: str, use_filename: bool = True) -> None:
        """Downloads attachment to designated filepath

        Args:
            download_path (str): The path to download the file to.
            use_filename (bool, optional): whether to use the file name supplied by Service-Now. Defaults to True.
        """
        
        if (not exists(download_path)):
            raise Exception(f"Invalid download path: {download_path}")
        
        if use_filename:
            download_path = join(download_path, self.FileName)
        
        _response = self.Client.get(self.DownloadLink)
        
        with open(download_path, "wb") as file:
            file.write(_response.content)
    
    @property
    def EncryptionContext(self) -> EncryptionContext:
        """Gets the encryption context
        """
        
        return EncryptionContext.fromString(self["encryption_context"].Value)
    
    @property
    def State(self) -> str:
        return self["state"].Value
    
    @property
    def Size(self) -> int:
        return int(self["size_bytes"].Value)

    @property
    def CompressedSize(self) -> int:
        return int(self["size_compressed"].Value)

    @property
    def TableSysId(self) -> str:
        return self["table_sys_id"].Value
    
    @property
    def Hash(self) -> str:
        return self["hash"].Value
    
    @property
    def ChunkSize(self) -> int:
        return int(self["chunk_size_bytes"].Value)

    @property
    def IsCompressed(self) -> bool:
        return bool(self["compressed"].Value)