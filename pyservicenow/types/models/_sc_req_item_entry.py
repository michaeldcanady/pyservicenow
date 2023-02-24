from __future__ import annotations

from datetime import datetime

from pyservicenow.types.models._ticket_entry import TicketEntry
from pyservicenow.types.models._sys_user_entry import User
from pyservicenow.types.enums import State, RequestItemPriority


class RequestedItem(TicketEntry):
    """Request Item Type"""

    @property
    def sys_id(self) -> str:
        return self.get("sys_id", str)

    @property
    def closed_by(self) -> User:
        """Gets Closed By"""

        return self.get("closed_by", User)

    @property
    def State(self) -> State:
        """Gets State"""

        return State(int(self["state"].actual_value))

    @property
    def active(self) -> bool:
        """Gets active"""

        return self.get("active", bool)

    @property
    def received(self) -> bool:
        """Gets recieved"""

        return self.get("received", bool)

    @property
    def priority(self) -> RequestItemPriority:
        """Gets priority"""

        return self.get("priority", RequestItemPriority)

    @property
    def cat_item(self) -> None:
        """Gets catalog item"""

        raise NotImplementedError("cat_item is not implemented")

    @property
    def assigned_to(self) -> User:
        """Gets assigned to"""

        return self.get("assigned_to", User)

    @property
    def start_date(self) -> datetime:
        """Gets start date"""

        return self.get("start_date", datetime)

    @property
    def short_description(self) -> str:
        """Gets short description"""

        return self.get("short_description", str)

    @short_description.setter
    def short_description(self, short_description: str) -> None:
        _old_value = self["short_description"]

        _old_value.actual_value = short_description

        self["short_description"] = _old_value

    @property
    def description(self) -> str:
        """Gets the description"""

        return self.get("description", str)

    @description.setter
    def description(self, value: str) -> None:
        _old_value = self["description"]

        _old_value.actual_value = value

        self["description"] = _old_value

    @property
    def request(self) -> None:
        """Gets the request"""

        raise NotImplementedError("request is not implemented")

    @property
    def assignment_group(self) -> None:
        """Get the assignment group"""

        raise NotImplementedError("Update is not implemented")

    def add_work_notes(self, work_notes: str) -> bool:
        """Adds work notes to the ticket"""

        raise NotImplementedError("add_work_notes is not implemented")

    def Update(self) -> None:
        """Updates the Service-Now Record"""

        raise NotImplementedError("Update is not implemented")
