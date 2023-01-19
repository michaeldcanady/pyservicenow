"""Houses Order By Enum"""

from enum import IntEnum, auto


class OrderBy(IntEnum):
    """Order By Enum"""

    ASC = auto()
    DESC = auto()


OrderBy.ASC.__doc__ = """Orders results ascendingly"""
OrderBy.DESC.__doc__ = """Order results decendingly"""
