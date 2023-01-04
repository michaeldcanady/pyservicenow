from typing import Generic, TypeVar, Type, get_args, final

A = TypeVar("A")

class AccessibleGeneric(Generic[A]):
    
    def __init__(self) -> None:
        super().__init__()
    
    @property
    @final
    def GenericType(self) -> Type[A]:
        """Gets the the type argument provided
        """
        
        _type: Type[A] = get_args(self.__orig_bases__[0])[0] # type: ignore  
              
        return _type