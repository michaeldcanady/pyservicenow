from pyservicenow.types.exceptions._py_snow_exception import PysnowException

class ResponseError(PysnowException):
    message = "<empty>"
    detail = "<empty>"

    def __init__(self, error):
        if "message" in error:
            self.message = error["message"] or self.message
        if "detail" in error:
            self.detail = error["detail"] or self.detail

    def __str__(self):
        return "Error in response. Message: %s, Details: %s" % (
            self.message,
            self.detail,
        )