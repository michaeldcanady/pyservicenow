from enum import IntEnum, auto
from strenum import UppercaseStrEnum

class HttpsMethods(UppercaseStrEnum):
    GET = auto()
    POST = auto()
    DELETE = auto()
    PATCH = auto()
    PUT = auto()