"""Houses current user model"""

from __future__ import annotations

from abc import abstractmethod

from typing import Dict

from pyservicenow.types.models._abstract_servicenow_entry import AbstractServiceNowEntry


class AbstractCurrentUser(AbstractServiceNowEntry):
    """Abstract Current User Type"""

    @property
    @abstractmethod
    def user_avatar(self) -> bytes:
        """Gets the avatar image

        Returns:
            bytes: The avatar image
        """

    @property
    @abstractmethod
    def user_sys_id(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

    @property
    @abstractmethod
    def user_name(self) -> str:
        """Gets the username

        Returns:
            str: The username
        """

    @property
    @abstractmethod
    def user_display_name(self) -> str:
        """Gets the display name

        Returns:
            str: The display name
        """

    @property
    @abstractmethod
    def user_initials(self) -> str:
        """Gets the initials

        Returns:
            str: The initials
        """