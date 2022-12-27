from typing import Dict

class Error(Exception):

    def __init__(self, message: str, detail: str) -> None:
        super().__init__()
        self._message = message
        self._detail = detail

    def asDict(self) -> Dict:
        return {
            "message": self._message,
            "detail": self._detail
        }

    def __str__(self) -> str:
        return str(self.asDict())

class ServiceNowServiceException(Exception):

    def __init__(self, inner_error: Error, status: str) -> None:
        self._inner_error = inner_error
        self._status = status

    def asDict(self) -> Dict:
        return {
            "error": self._inner_error.asDict(),
            "status": self._status
        }

    def __str__(self) -> str:
        return str(self.asDict())