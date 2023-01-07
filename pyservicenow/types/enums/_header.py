"""Contains header enum"""

from strenum import StrEnum


class Header(StrEnum):
    """possible header keys that can be used"""
    ACCEPT = "Accept"

Header.ACCEPT.__doc__ = """Defines the type of body the API should expect"""
