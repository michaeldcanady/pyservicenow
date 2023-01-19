"""Houses Username Password Credential"""

from base64 import b64encode
from typing import Union
from pyrestsdk.credential import AbstractBasicCredential


class UsernamePasswordCredential(AbstractBasicCredential):
    """Username Password Credential Type"""
    
    __slots__ = ["username", "password"]

    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:

        super().__init__()

        self.username = username
        self.password = password

    def to_native_string(self, string: Union[str, bytes], encoding="ascii") -> str:
        """Given a string object, regardless of type, returns a representation of
        that string in the native string type, encoding and decoding where
        necessary. This assumes ASCII unless told otherwise.
        """
        if isinstance(string, str):
            return string
        return string.decode(encoding)

    def get_basic(self) -> str:

        username = self.username.encode("latin1")
        password = self.password.encode("latin1")

        return self.to_native_string(b64encode(b":".join((username, password))).strip())
