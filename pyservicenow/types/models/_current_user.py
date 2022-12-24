from typing import Dict, Optional

# internal imports
from ._servicenow_entry import ServiceNowEntry

class CurrentUser(ServiceNowEntry):

    #_client

    def __init__(self, _value: ServiceNowEntry = ServiceNowEntry(), client = None) -> None:
        super().__init__(_value)
        self._client = client

    @property
    def UserProfile(self) -> bytes:
        """Gets the avatar image

        Returns:
            bytes: The avatar image
        """

        if self._client is None:
            raise Exception("'Client' can't be 'None'")

        profile_id = self["user_avatar"].Value

        return self._client.CustomEndpoint(profile_id).content # type: ignore

    @property
    def SysId(self) -> str:
        """Gets the sys id

        Returns:
            str: The sys id
        """

        return self["user_sys_id"].Value

    @property
    def UserName(self) -> str:
        """Gets the username

        Returns:
            str: The username
        """

        return self["user_name"].Value

    @property
    def DisplayName(self) -> str:
        """Gets the display name

        Returns:
            str: The display name
        """

        return self["user_display_name"].Value

    @property
    def Initials(self) -> str:
        """Gets the initials

        Returns:
            str: The initials
        """

        return self["user_initials"].Value

    @classmethod
    def fromJson(cls, entry: Dict, client) -> 'CurrentUser':
        """Converts entry from dictionary to new CurrentUser.

        Args:
            entry (Dict): The entry to convert
            client (AbstractServiceClient): The client to be usable by the object

        Returns:
            CurrentUser: The current user
        """

        _child = super().fromJson(entry)

        new = cls(_child, client)

        return new