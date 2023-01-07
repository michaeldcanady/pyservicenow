"""Houses the Service-Now Property"""

from json import dumps
from typing import Dict, Any


class ServiceNowProperty:
    """Service-Now Property type"""

    def __init__(self) -> None:
        self._display_value: str = ""
        self._value: str = ""
        self._link: str = ""

    @property
    def display_value(self) -> str:
        """Gets/Sets the display value

        Returns:
            str: The display value
        """

        return self._display_value

    @display_value.setter
    def display_value(self, value: str) -> None:
        self._display_value = value

    @property
    def value_link(self) -> str:
        """Gets/Sets the link

        Returns:
            str: The link
        """

        return self._link

    @value_link.setter
    def value_link(self, value: str) -> None:
        self._link = value

    @property
    def actual_value(self) -> str:
        """Gets/Sets the value

        Returns:
            str: The value
        """

        return self._value

    @actual_value.setter
    def actual_value(self, value: str) -> None:
        self._value = value

    def as_dict(self) -> Dict[str, Any]:
        """Gets object as dict"""

        return {
            "display_value": self.display_value,
            "value": self.actual_value,
            "link": self.value_link,
        }

    def __json__(self) -> str:
        return dumps(self.as_dict())
