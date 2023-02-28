"""Houses the Service-Now Property"""

from typing import TypeVar, Type, Dict, Any, Union

from abc import abstractmethod

from json import dumps

S = TypeVar("S", bound="AbstractServiceNowProperty")


class AbstractServiceNowProperty:
    """Service-Now Property type"""

    _display_value: str
    _value: str
    _link: str

    @property
    @abstractmethod
    def display_value(self) -> str:
        """Gets/Sets the display value

        Returns:
            str: The display value
        """

    @display_value.setter
    @abstractmethod
    def display_value(self, value: str) -> None:
        ...

    @property
    @abstractmethod
    def value_link(self) -> str:
        """Gets/Sets the link

        Returns:
            str: The link
        """

    @value_link.setter
    @abstractmethod
    def value_link(self, value: str) -> None:
        ...

    @property
    @abstractmethod
    def actual_value(self) -> str:
        """Gets/Sets the value

        Returns:
            str: The value
        """

    @actual_value.setter
    @abstractmethod
    def actual_value(self, value: str) -> None:
        ...

    @property
    @abstractmethod
    def as_dict(self) -> Dict[str, Any]:
        """Gets the property as dict

        Returns:
            Dict[str, Any]: The property as dict
        """
    
    @abstractmethod
    def __json__(self) -> str:
        """Gets the JSON of the ServiceNow Property

        Returns:
            str: The JSON of the ServiceNow Property
        """
        
    @classmethod
    @abstractmethod
    def __fromjson__(cls: Type[S], value: Union[str, Dict]) -> S:
        """Converts the value to a ServiceNow Property

        Args:
            cls (Type[S]): The ServiceNow Property
            value (Union[str, Dict]): The JSON representaion

        Returns:
            S: The ServiceNow Property
        """