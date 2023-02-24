"""Houses User"""

from datetime import datetime

from pyservicenow.types.models._servicenow_property import ServiceNowProperty
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry


class User(ServiceNowEntry):
    """User Type"""

    @property
    def Name(self) -> str:
        """Gets the name"""

        return self.get("name", str)

    @Name.setter
    def Name(self, name: str) -> None:
        _value = ServiceNowProperty()
        _value.display_value = name

        self["name"] = _value

    @property
    def calendar_integration(self) -> str:
        """Gets the calendar integration"""

        return self.get("calendar_integration", str)

    @property
    def last_login_time(self) -> datetime:
        """Gets the last login time"""

        return self.get("last_login_time", datetime)

    @property
    def hashed_user_id(self) -> str:
        """Gets the hashed user id"""

        return self.get("hashed_user_id", str)

    @property
    def Source(self) -> str:
        """Gets the source"""

        return self.get("source", str)

    @property
    def sys_updated_on(self) -> datetime:
        """Gets the updated on"""

        return self.get("sys_updated_on", datetime)

    @property
    def web_service_access_only(self) -> bool:
        """Gets the web service access only"""

        return self.get("web_service_access_only", bool)

    @property
    def notification(self) -> int:
        """Gets the notification"""

        return self.get("notification", int)

    @property
    def enable_multifactor_authn(self) -> bool:
        """Gets if multifactor authentication is enabled"""

        return self.get("enable_multifactor_authn", bool)

    @property
    def sys_updated_by(self) -> str:
        """Gets updated by"""

        return self.get("sys_updated_by", str)

    @property
    def sso_source(self) -> str:
        """Gets the SSO Source"""

        return self.get("sso_source", str)

    @property
    def sys_created_on(self) -> datetime:
        """Gets created on date"""

        return self.get("sys_created_on", datetime)

    @property
    def Domain(self) -> None:
        """Gets domain"""

        raise NotImplementedError("Domain is not implemented")

    @property
    def State(self) -> str:
        """Gets the state"""

        return self.get("state", str)

    @property
    def vip(self) -> bool:
        """Gets if VIP"""

        return self.get("vip", bool)

    @property
    def sys_created_by(self) -> str:
        """Gets created by"""

        return self.get("sys_created_by", str)

    @property
    def active(self) -> bool:
        """Gets if active"""

        return self.get("active", bool)

    @property
    def phone(self) -> str:
        """Gets the phone"""

        return self.get("phone", str)

    @property
    def employee_number(self) -> str:
        """Gets the employee number"""

        return self.get("employee_number", str)

    @property
    def user_name(self) -> str:
        """Gets the user name"""

        return self.get("user_name", str)

    @property
    def internal_integration_user(self) -> bool:
        """Gets if an internal integration user"""

        return self.get("internal_integration_user", bool)

    @property
    def ldap_server(self) -> None:
        """Gets the LDAP Server"""

        raise NotImplementedError("LDAPServer")

    @property
    def first_name(self) -> str:
        """Gets the first name"""

        return self.get("first_name", str)

    @property
    def email(self) -> str:
        """Gets the email"""

        return self.get("email", str)

    @property
    def Auditor(self) -> bool:
        """Gets if auditor"""

        return self.get("auditor", bool)

    @property
    def last_name(self) -> str:
        """Gets the last name"""

        return self.get("last_name", str)
