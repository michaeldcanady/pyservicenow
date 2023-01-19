"""Houses attachment Entry Model"""

from __future__ import annotations
from os.path import exists, join
from typing import Dict
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry
from pyservicenow.types.enums import EncryptionContext

class AttachmentEntry(ServiceNowEntry):
    """Attachment Entry Type"""

    @property
    def content_type(self):
        """Gets the content type of the associated attachment file."""

        return self["content_type"].actual_value

    @property
    def file_name(self) -> str:
        """Get the file name of the attachment"""

        return self["file_name"].actual_value

    @property
    def sys_tags(self) -> str:
        """Gets any system tags associated with the attachment file"""

        return self["sys_tags"].actual_value

    @property
    def table_name(self) -> str:
        """Gets the table name it's attached to"""

        return self["table_name"].actual_value

    @property
    def download_link(self) -> str:
        """Gets the download URL of the attachment on the ServiceNow instance"""

        return self["download_link"].actual_value

    def get_record(self) -> ServiceNowEntry:
        """Gets the record the attachment is associated with"""

        return self.Client.Now().Table(self.table_name).id(self.table_sys_id).Get.Invoke

    def download_file(self, download_path: str, use_filename: bool = True) -> None:
        """Downloads attachment to designated filepath

        Args:
            download_path (str): The path to download the file to.
            use_filename (bool, optional):
            whether to use the file namesupplied by Service-Now. Defaults to True.
        """

        if not exists(download_path):
            raise Exception(f"Invalid download path: {download_path}")

        if use_filename:
            download_path = join(download_path, self.file_name)

        _response = self.Client.get(self.download_link)

        with open(download_path, "wb") as file:
            file.write(_response.content)

    @property
    def encryption_context(self) -> EncryptionContext:
        """Gets the encryption context"""
        return EncryptionContext.from_string(self["encryption_context"].actual_value)

    @property
    def file_state(self) -> str:
        """Gets the state of the attachment"""
        return self["state"].actual_value

    @property
    def size_bytes(self) -> int:
        """Gets the size of the attachment"""
        return int(self["size_bytes"].actual_value)

    @property
    def compressed_size(self) -> int:
        """Gets the size of the compressed attachment file. If the file is not compressed, empty."""
        return int(self["size_compressed"].actual_value)

    @property
    def table_sys_id(self) -> str:
        """Gets the sys_id of the table associated with the attachment"""
        return self["table_sys_id"].actual_value

    @property
    def file_hash(self) -> str:
        """Gets the file hash of the attachment"""
        return self["hash"].actual_value

    @property
    def chunk_size_bytes(self) -> int:
        """Gets the chunk size of the attachment in bytes"""
        return int(self["chunk_size_bytes"].actual_value)

    @property
    def is_compressed(self) -> bool:
        """Gets whether the file has been compressed or not"""
        return bool(self["compressed"].actual_value)

    @property
    def Json(self) -> Dict:
        """Gets the object as it's dict representation"""
        return super().Json