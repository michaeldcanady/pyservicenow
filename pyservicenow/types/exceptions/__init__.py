from pyservicenow.types.exceptions._unexpected_return_type import UnexpectedReturnType
from pyservicenow.types.exceptions._py_snow_exception import PysnowException
from pyservicenow.types.exceptions._unexpected_response_format import UnexpectedResponseFormat
from pyservicenow.types.exceptions._invalid_usage import InvalidUsage
from pyservicenow.types.exceptions._response_error import ResponseError
from pyservicenow.types.exceptions._missing_result import MissingResult
from pyservicenow.types.exceptions._no_results import NoResults


class EmptyContent(PysnowException):
    pass


class MultipleResults(PysnowException):
    pass


class MissingToken(PysnowException):
    pass


class TokenCreateError(PysnowException):
    def __init__(self, error, description, status_code):
        self.error = error
        self.description = description
        self.snow_status_code = status_code


class QueryTypeError(PysnowException):
    pass


class QueryMissingField(PysnowException):
    pass


class QueryEmpty(PysnowException):
    pass


class QueryExpressionError(PysnowException):
    pass


class QueryMultipleExpressions(PysnowException):
    pass
