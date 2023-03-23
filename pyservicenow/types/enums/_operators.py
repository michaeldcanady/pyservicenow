"""Houses Operators"""

from strenum import StrEnum


class Operators:
    """Operators Enum"""

    class Comparison(StrEnum):
        """Comparision Enum"""

        NULL = ""
        
        EQUALS = "="
        NOTEQUALS = "!="
        
        IN = "IN"
        NOTIN = "NOT IN"
        
        LIKE = "LIKE"
        NOTLIKE = "NOT LIKE"
        
        STARTSWITH = "STARTSWITH"
        ENDSWITH = "ENDSWITH"
        
        LESSEROREQUAL = "<="
        GREATEROREQUAL = ">="
        
        ISEMPTY = "ISEMPTY"
        ISNOTEMPTY = "ISNOTEMPTY"
        ISANYTHING = "ANYTHING"
        
        BETWEEN = "BETWEEN"
        
        ISSAME = "SAMEAS"
        ISDIFFERENT = "NSAMEAS"

    class Logical(StrEnum):
        """Logical Operator Enum"""

        AND = "^"
        OR = "^OR"
        NEWQUERY = "^NQ"
        ENDQUERY = "^EQ"


Operators.Comparison.NULL.__doc__ = """No operator selected"""
Operators.Comparison.EQUALS.__doc__ = """Equals Operator"""
Operators.Comparison.IN.__doc__ = """In operator"""
Operators.Comparison.LIKE.__doc__ = """Like operator"""
Operators.Logical.AND.__doc__ = """And operator"""
Operators.Logical.OR.__doc__ = """Or operator"""
Operators.Logical.NEWQUERY.__doc__ = """New Query Operator"""
