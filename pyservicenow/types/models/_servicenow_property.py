
class ServiceNowProperty(object):

    _display_value: str = ""
    _value: str = ""
    _link: str = ""

    def __init__(self) -> None:
        pass

    @property
    def DisplayValue(self) -> str:
        """Gets/Sets the display value

        Returns:
            str: The display value
        """

        return self._display_value
    
    @DisplayValue.setter
    def DisplayValue(self, value: str) -> None:
        self._display_value = value
    
    @property
    def Link(self) -> str:
        """Gets/Sets the link

        Returns:
            str: The link
        """

        return self._link
    
    @Link.setter
    def Link(self, value: str) -> None:
        self._link = value

    @property
    def Value(self) -> str:
        """Gets/Sets the value

        Returns:
            str: The value
        """

        return self._value

    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value