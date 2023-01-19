from pyservicenow.types.enums import Operators
from pyservicenow.types.models._base_query_builder import BaseQueryBuilder

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

        i, n = 0, len(query)

        while i < n:

            if (
                (query[i] == Operators.Comparison.EQUALS)
                or (query[i : i + 1] == Operators.Comparison.IN)
                or (query[i : i + 4] == Operators.Comparison.LIKE)
            ):  # get the operator
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
            elif query[i] == "^":

                oper_dict = {
                    Operators.Comparison.EQUALS: query_builder.equals,
                    Operators.Comparison.IN: query_builder.IN,
                    Operators.Comparison.LIKE: query_builder.contains,
                }

                oper = oper_dict[operator]

                oper(value)

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

            elif operator != Operators.Comparison.NULL:  # get the value
                value += query[i]
                if i == n - 1:
                    oper_dict = {
                        Operators.Comparison.EQUALS: query_builder.equals,
                        Operators.Comparison.IN: query_builder.IN,
                        Operators.Comparison.LIKE: query_builder.contains,
                    }

                    oper = oper_dict[operator]

                    oper(value)

            else:  # get the field
                field += query[i]

            i += 1

        return query_builder
