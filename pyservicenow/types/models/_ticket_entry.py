"""Houses Ticket Entry"""

from __future__ import annotations

from typing import TypeVar

from datetime import datetime

from pyservicenow.types.models._servicenow_entry import ServiceNowEntry
from pyservicenow.types.models._sys_user_entry import User

T = TypeVar("T")


class TicketEntry(ServiceNowEntry):
    """Ticket Entry Type"""

    @property
    def parent(self) -> str:
        """Gets the parent"""

        return self.get("parent", str)

    @property
    def number(self) -> str:
        """Gets the number"""

        return self.get("number", str)

    @property
    def caused_by(self) -> str:
        """Gets caused by"""

        return self.get("caused_by", str)

    @property
    def upon_reject(self) -> str:
        """Gets upon reject"""

        return self.get("upon_reject", str)

    @property
    def requested_for(self) -> User:
        """Get Request For user"""

        return self.get("requested_for", User)

    @property
    def sys_updated_on(self) -> datetime:
        """Get Updated On date time"""

        return self.get("sys_updated_on", datetime)

    def ClientIsNone(self) -> bool:
        """Gets if the client is None"""

        return self.Client is None
