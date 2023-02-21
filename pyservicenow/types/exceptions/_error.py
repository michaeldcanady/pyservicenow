from typing import Dict

class Error(Exception):
    
    def __init__(self, detail: str, message: str) -> None:
        super().__init__(None)
        
        self._detail = detail
        self._message = message
        
    def __str__(self) -> str:
        return f"detail: {self._detail}, message: {self._message}"
    
    @classmethod
    def from_json(cls, raw_json: Dict[str, str]) -> 'Error':
        
        detail = raw_json["detail"]
        message = raw_json["message"]
        
        return cls(detail, message)