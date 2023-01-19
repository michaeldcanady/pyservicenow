"""Houses Display Value Enum"""

from strenum import StrEnum


class DisplayValue(StrEnum):
    """Determines the type of data returned,
    either the actual values from the database or the display values of the fields.
    Display values are manipulated based on the actual value in the database and
    user or system settings and preferences.
     If returning display values, the value that is returned is dependent on the field type.
    """
    TRUE = "true"
    FALSE = "false"
    ALL = "all"

DisplayValue.TRUE.__doc__ = """Returns the display values for all fields."""
DisplayValue.FALSE.__doc__ = """false: Returns the actual values from the database."""
DisplayValue.ALL.__doc__ = """Returns both actual and display values."""
