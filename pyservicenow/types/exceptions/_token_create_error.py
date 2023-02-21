"""Houses Token Create Error Type"""

from pyservicenow.types.exceptions._py_snow_exception import PysnowException


class TokenCreateError(PysnowException):
    """Token Create Error Type"""

    def __init__(self, error, description, status_code):
        self.error = error
        self.description = description
        self.snow_status_code = status_code
