from typing import Dict, TypeVar, Type, Any

S = TypeVar('S', bound='BaseEntity')


class BaseEntity(object):

    __client: Any

    def Json(self) -> Dict: ...

    @classmethod
    def fromJson(cls: Type[S], entry: Dict) -> 'BaseEntity': ...
