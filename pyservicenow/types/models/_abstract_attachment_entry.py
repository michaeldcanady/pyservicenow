"""Houses abstract attachment Entry Model"""

from __future__ import annotations

from abc import abstractmethod

from os.path import exists, join

from typing import Dict, Any

from pyservicenow.types.models._abstract_servicenow_entry import AbstractServiceNowEntry

from pyservicenow.types.models._servicenow_entry import ServiceNowEntry

from pyservicenow.types.enums import EncryptionContext


class AbstractAttachmentEntry(AbstractServiceNowEntry):
    """Abstract Attachment Entry Type"""

    @property
    @abstractmethod
    def content_type(self) -> str:
        """Gets the content type of the associated attachment file.

        Returns:
            str: The content type of the associated attachment file.
        """

    @property
    @abstractmethod
    def file_name(self) -> str:
        """Get the file name of the attachment

        Returns:
            str: The file name of the attachment
        """

    @property
    @abstractmethod
    def sys_tags(self) -> str:
        """Gets any system tags associated with the attachment file

        Returns:
            str: Any system tags associated with the attachment file
        """

    @property
    @abstractmethod
    def table_name(self) -> str:
        """Gets the table name it's attached to

        Returns:
            str: The table name it's attached to
        """

    @property
    @abstractmethod
    def download_link(self) -> str:
        """Gets the download URL of the attachment on the ServiceNow instance

        Returns:
            str: The download URL of the attachment on the ServiceNow instance
        """
        
    @property
    @abstractmethod
    def encryption_context(self) -> EncryptionContext:
        """Gets the encryption context

        Returns:
            EncryptionContext: The encryption context
        """
        
    @property
    @abstractmethod
    def file_state(self) -> str:
        """Gets the state of the attachment

        Returns:
            str: The state of the attachment
        """
        
    @property
    @abstractmethod
    def size_bytes(self) -> int:
        """Gets the size of the attachment

        Returns:
            int: The size of the attachment
        """
        
    @property
    @abstractmethod
    def compressed_size(self) -> int:
        """Gets the size of the compressed attachment file. If the file is not compressed, empty.

        Returns:
            int: The size of the compressed attachment file. If the file is not compressed, empty.
        """
        
    @property
    @abstractmethod
    def table_sys_id(self) -> str:
        """Gets the sys_id of the table associated with the attachment

        Returns:
            str: _description_
        """
        
    @property
    @abstractmethod
    def file_hash(self) -> str:
        """Gets the file hash of the attachment

        Returns:
            str: The file hash of the attachment
        """
        
    @property
    @abstractmethod
    def chunk_size_bytes(self) -> int:
        """Gets the chunk size of the attachment in bytes

        Returns:
            int: The chunk size of the attachment in bytes
        """
        
    @property
    @abstractmethod
    def is_compressed(self) -> bool:
        """Gets whether the file has been compressed or not

        Returns:
            bool: Whether the file has been compressed or not
        """
    
    @abstractmethod
    def update_object(self) -> bool:
        """Updates the attachment entry

        Returns:
            bool: If successfully updated
        """
    
    @abstractmethod
    def get_record(self) -> ServiceNowEntry:
        """Gets the record the attachment is associated with

        Returns:
            ServiceNowEntry: The record the attachment is associated with
        """
    
    @abstractmethod
    def download_file(self, download_path: str, use_filename: bool = True) -> None:
        """Downloads attachment to designated filepath

        Args:
            download_path (str): The path to download the file to.
            use_filename (bool, optional): whether to use the file
            namesupplied by Service-Now. Defaults to True.
        """