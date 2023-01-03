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
        """Gets the content type of the associated attachment file.
        """
        
        return self["content_type"].Value

    @property
    def FileName(self) -> str:
        """Get the file name of the attachment
        """
        
        return self["file_name"].Value
    
    @property
    def Tags(self) -> str:
        """Gets any system tags associated with the attachment file
        """
        
        return self["sys_tags"].Value

    @property
    def TableName(self) -> str:
        """Gets the table name it's attached to
        """
        
        return self["table_name"].Value

    @property
    def DownloadLink(self) -> str:
        """Gets the download URL of the attachment on the ServiceNow instance
        """
        
        return self["download_link"].Value
    
    def GetRecord(self) -> ServiceNowEntry:
        """Gets the record the attachment is associated with
        """
        
        return self.Client.Now().Table(self.TableName).id(self.TableSysId).Get.Invoke
    
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
        """Gets the size of the attachment
        """
        
        return int(self["size_bytes"].Value)

    @property
    def CompressedSize(self) -> int:
        """Gets the size of the compressed attachment file. If the file is not compressed, empty.
        """
        
        return int(self["size_compressed"].Value)

    @property
    def TableSysId(self) -> str:
        """Gets the sys_id of the table associated with the attachment
        """
        
        return self["table_sys_id"].Value
    
    @property
    def Hash(self) -> str:
        return self["hash"].Value
    
    @property
    def ChunkSize(self) -> int:
        return int(self["chunk_size_bytes"].Value)

    @property
    def IsCompressed(self) -> bool:
        """Gets whether the file has been compressed or not
        """
        
        return bool(self["compressed"].Value)