"""Houses View Enum"""

from strenum import StrEnum


class View(StrEnum):
    """View type enum"""
    DESKTOP = "desktop"
    MOBILE = "mobile"
    BOTH = "both"
