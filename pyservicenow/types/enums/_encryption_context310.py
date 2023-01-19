"""Houses Encryption Context Enum"""

from enum import IntEnum, auto

# https://docs.servicenow.com/bundle/rome-platform-security/page/administer/encryption/concept/c_EncryptionSupport.html
class EncryptionContext(IntEnum):
    """Encryption Context Enum"""

    NULL = auto()
    SINGLE = auto()
    MULTIPLE = auto()

    @classmethod
    def from_string(cls, value: str) -> "EncryptionContext":
        """Converts string to encryption context"""

        match (value.casefold()):

            case n if n == "" or n is None:
                return EncryptionContext.NULL
            case "single":
                return EncryptionContext.SINGLE
            case "multiple":
                return EncryptionContext.MULTIPLE
            case other:
                raise Exception(f"unknown value {value}")

    def __str__(self) -> str:
        return self.name


EncryptionContext.NULL.__doc__ = """
No encryption context set"""
EncryptionContext.SINGLE.__doc__ = """
The field is encrypted with the encryption context defined in the Encryption context field.
Users who do not have the encryption context cannot view or update field values."""
EncryptionContext.MULTIPLE.__doc__ = """
The field is encrypted with the encryption context of the first user to enter data.
If the user has two or more encryption contexts, the context defined in the encryption context selector is used.
Because the encryption context is set on a per record basis, fields in a list can have different encryption contexts.
However, within a single record, the field can be encrypted by only one context.

When an Encrypted Text field is created, an encrypted field configuration is created with the multiple encryption contexts method.
Encrypted Text fields and fields encrypted with the multiple encryption contexts method behave the same."""
