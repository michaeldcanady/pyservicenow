from sys import version_info

from pyservicenow.types.enums import Operators
from pyservicenow.types.models._base_query_builder import BaseQueryBuilder

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class QueryBuilder(BaseQueryBuilder):

    @classmethod
    def parse(cls, query: str) -> Self:
        """Parses query into new QueryBuilder

        Args:
            query (str): The query to parse

        Returns:
            QueryBuilder: The new QueryBuilder object
        """

        query_builder = cls()

        field = ""
        operator = Operators.Comparison.NULL
        value = ""

        i, l = 0, len(query)

        while i < l:

            match (query):
                case n if (n[i] == Operators.Comparison.EQUALS) or (
                    n[i : i + 1] == Operators.Comparison.IN
                ) or (n[i : i + 4] == Operators.Comparison.LIKE):
                    query_builder.field(field)
                    if query[i] == Operators.Comparison.EQUALS:
                        operator = Operators.Comparison.EQUALS
                    elif query[i : i + 2] == Operators.Comparison.IN:
                        i += 2
                        operator = Operators.Comparison.IN
                        continue
                    elif query[i : i + 4] == Operators.Comparison.LIKE:
                        i += 4
                        operator = Operators.Comparison.LIKE
                        continue
                    field = ""
                case n if n[i] == "^":

                    match (operator):
                        case Operators.Comparison.EQUALS:
                            query_builder.equals(value)
                        case Operators.Comparison.IN:
                            query_builder.IN(value)
                        case Operators.Comparison.LIKE:
                            query_builder.contains(value)

                    if query[i : i + 4] == Operators.Logical.NEWQUERY:
                        query_builder.NQ
                        i += 4
                        continue
                    elif query[i : i + 4] == Operators.Logical.OR:
                        query_builder.OR
                        i += 4
                        continue
                    else:
                        query_builder.AND

                    value = ""
                    operator = Operators.Comparison.NULL

                case _ if operator != Operators.Comparison.NULL:
                    value += query[i]
                    if i == l - 1:
                        match (operator):
                            case Operators.Comparison.EQUALS:
                                query_builder.equals(value)
                            case Operators.Comparison.IN:
                                query_builder.IN(value)
                            case Operators.Comparison.LIKE:
                                query_builder.contains(value)
                case other:
                    field += query[i]

            i += 1

        return query_builder
