"""Houses Mime Type Name Enum"""

from strenum import StrEnum


class MimeTypeName:
    """Mime Type type"""
    class Application(StrEnum):
        """Application Mime Type enum"""
        INVALID = "invalid"
        JSON = "application/json"
        XML = "application/xml"

    @classmethod
    def from_string(cls, value: str) -> Application:
        """Converts value to valid Mime Type enum value"""
        for item in iter(MimeTypeName.Application):
            if value.casefold() == item.casefold():
                return item
        return MimeTypeName.Application.INVALID
