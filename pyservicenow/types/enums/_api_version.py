"""Houses API Version Enum"""

from enum import IntEnum, auto


class APIVersion(IntEnum):
    """Version of the Service-Now API"""
    NULL = auto()
    V1 = auto()
    V2 = auto()

APIVersion.NULL.__doc__ = """No API Version selected; uses default version"""
APIVersion.V1.__doc__ = """Version 1.0 API Selected"""
APIVersion.V2.__doc__ = """Version 2.0 API Selected"""
