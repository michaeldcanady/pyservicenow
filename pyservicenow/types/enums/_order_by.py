"""Houses Order By Enum"""

from enum import IntEnum, auto


class OrderBy(IntEnum):
    """Order By Enum"""

    ASC = auto()
    DESC = auto()
    
    def __str__(self) -> str:
        
        if self == OrderBy.ASC:
            return "ORDERBY"
        elif self == OrderBy.DESC:
            return "ORDERBYDESC"
        else:
            raise ValueError(f"{self} is not a valid type")
        


OrderBy.ASC.__doc__ = """Orders results ascendingly"""
OrderBy.DESC.__doc__ = """Order results decendingly"""
