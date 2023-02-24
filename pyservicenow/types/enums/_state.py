"""Houses State"""

from enum import IntEnum


class State(IntEnum):
    """Service-Now Ticket State Enum"""

    INVALID = -1
    NULL = 0
    OPEN = 1
    WORKINPROGRESS = 2
    ONHOLD = 11
    CLOSED = 3
    CANCELLED = 7

    def __str__(self) -> str:
        _string_value_dict = {
            State.NULL: "Null",
            State.OPEN: "Open",
            State.WORKINPROGRESS: "Work In Progress",
            State.ONHOLD: "On Hold",
            State.CLOSED: "Closed",
            State.CANCELLED: "Cancelled"
        }

        return _string_value_dict.get(self, "Null")

    def __json__(self) -> str:
        return str(self.value)


State.INVALID.__doc__ = """The state of the ticket is invalid"""
State.NULL.__doc__ = """State is unset"""
State.OPEN.__doc__ = """The Ticket is in the open state"""
State.WORKINPROGRESS.__doc__ = """The Ticket is in the Work In Progress state"""
State.ONHOLD.__doc__ = """The Ticket is in the On Hold state"""
State.CLOSED.__doc__ = """The Ticket is in the Closed state"""
State.CANCELLED.__doc__ = """The Ticket is in the cancelled state"""
