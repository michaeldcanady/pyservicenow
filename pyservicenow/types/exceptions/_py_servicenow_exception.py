"""Houses py Service-Now Exception"""

from typing import Dict, Any

from pyservicenow.types.exceptions._error import Error

class PyServiceNowException(Exception):
    
    def __init__(self, error: Error, status: str) -> None:
        super().__init__(None)
        
        self._error = error
        self._status = status
        
    def __str__(self) -> str:
        return f"error: {self._error}, status: {self._status}"
    
    @classmethod
    def from_json(cls, raw_json: Dict[str, Any]) -> 'PyServiceNowException':
        
        raw_error_json = raw_json["error"]
        status = raw_json["status"]
        
        error = Error.from_json(raw_error_json)
        
        return cls(error, status)