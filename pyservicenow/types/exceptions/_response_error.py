"""Houses Response Error Type"""

from typing import Dict, Any

from pyservicenow.types.exceptions._py_snow_exception import PysnowException


class ResponseError(PysnowException):
    """Response Error Type"""

    message = "<empty>"
    detail = "<empty>"

    def __init__(self, error: Dict[str, Any]):
        if "message" in error:
            self.message = error["message"] or self.message
        if "detail" in error:
            self.detail = error["detail"] or self.detail

    def __str__(self) -> str:
        return f"Error in response. Message: {self.message}, Details: {self.detail}"
