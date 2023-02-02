"""Houses the Service-Now Property"""
from typing import TypeVar, Type

from json import dumps
from typing import Dict, Any, Union

S = TypeVar("S", bound="ServiceNowProperty")


class ServiceNowProperty:
    """Service-Now Property type"""
    
    #__slots__ = ["_display_value", "_value", "_link"]

    _display_value: str
    _value: str
    _link: str

    def __init__(self) -> None:
        self._display_value = ""
        self._value = ""
        self._link = ""

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
    
    @classmethod
    def __fromjson__(cls: Type[S], value: Union[str, Dict]) -> S:
        
        _value = cls()
        
        if not isinstance(value, str) and not isinstance(value, dict):
            return _value
        
        if value is None:
            pass
        elif isinstance(value, str):
            _value.actual_value = value
        else:
            _value.display_value = value.get("display_value", "")
            _value.actual_value = value.get("value", "")
            _value.value_link = value.get("link", "")
            
        return _value
