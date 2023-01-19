"""Houses current user model"""

from __future__ import annotations
from typing import Dict
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry


class CurrentUser(ServiceNowEntry):
    """Current User Type"""

    @property
    def user_avatar(self) -> bytes:
        """Gets the avatar image

        Returns:
            bytes: The avatar image
        """
        profile_id = self["user_avatar"].actual_value

        return self.Client.CustomEndpoint(profile_id).content  # type: ignore

    @property
    def user_sys_id(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """
        return self["user_sys_id"].actual_value

    @property
    def user_name(self) -> str:
        """Gets the username

        Returns:
            str: The username
        """
        return self["user_name"].actual_value

    @property
    def user_display_name(self) -> str:
        """Gets the display name

        Returns:
            str: The display name
        """
        return self["user_display_name"].actual_value

    @property
    def user_initials(self) -> str:
        """Gets the initials

        Returns:
            str: The initials
        """
        return self["user_initials"].actual_value

    @property
    def as_dict(self) -> Dict:
        """Gets the object as it's dict representation"""
        return {
            "user_initials": self["user_initials"].as_dict(),
            "user_display_name": self["user_display_name"].as_dict(),
            "user_name": self["user_name"].as_dict(),
            "user_sys_id": self["user_sys_id"].as_dict(),
        }

    @property
    def Json(self) -> Dict:
        """Gets the object as it's dict representation"""
        return self.as_dict

    def update_object(self) -> bool:
        """Current User cannot be updated"""

        return False
