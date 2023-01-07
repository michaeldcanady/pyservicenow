"""Houses all credentials for authenticating to Service-Now"""

from pyservicenow.core.credential._username_password_credential import (
    UsernamePasswordCredential,
)

__all__ = ["UsernamePasswordCredential"]
