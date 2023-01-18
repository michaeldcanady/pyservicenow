from typing import Union, List
import inspect
from pyservicenow.types.enums import OrderBy, Operators

# internal imports
from ..exceptions import (
    QueryEmpty,
    QueryExpressionError,
    QueryMissingField,
    QueryMultipleExpressions,
)


class QueryBuilder:
    """Query Builder type"""

    __slots__ = ["_query", "current_field", "c_oper", "l_oper"]

    _query: List
    current_field: str
    c_oper: Operators.Comparison
    l_oper: Operators.Logical

    def __init__(self) -> None:
        """Constructs a new query builder"""

        self._query = []
        self.current_field = None
        self.c_oper = None
        self.l_oper = None

    @classmethod
    def parse(cls, query: str) -> "QueryBuilder":
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

    def field(self, field: str) -> "QueryBuilder":
        """Sets the field to operate on

        Args:
            field (str): The field

        Returns:
            QueryBuilder: The query builder
        """

        self.current_field = field

        return self

    def order_by(self, direction: OrderBy) -> "QueryBuilder":
        """Sets the order by direction

        Args:
            direction (OrderBy): Direction to order results by

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            QueryBuilder: The current QueryBuilder object
        """

        if direction == OrderBy.ASC:
            self._query.append("ORDERBY{0}".format(self.current_field))
        elif direction == OrderBy.DESC:
            self._query.append("ORDERBYDESC{0}".format(self.current_field))

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.c_oper = _f_back.f_code.co_name

        return self

    def equals(self, data: Union[str, int]) -> "QueryBuilder":
        """Adds new `=` condition"""

        return self._add_condition(Operators.Comparison.EQUALS, data, types=[int, str])

    def IN(self, data: List) -> "QueryBuilder":
        """Adds new `IN` condition"""

        return self._add_condition(Operators.Comparison.IN, ",".join(map(str, data)), types=[str])

    def contains(self, contains: str):
        """Adds new `LIKE` condition
        """

        return self._add_condition(Operators.Comparison.LIKE, contains, types=[str])

    @property
    def AND(self) -> "QueryBuilder":
        """Adds an and-operator"""
        return self._add_logical_operator(Operators.Logical.AND)

    @property
    def OR(self) -> "QueryBuilder":
        """Adds an or-operator"""
        return self._add_logical_operator(Operators.Logical.OR)

    @property
    def NQ(self) -> "QueryBuilder":
        """Adds a NQ-operator (new query)"""
        return self._add_logical_operator(Operators.Logical.NEWQUERY)

    def __str__(self) -> str:
        """String representation of the query object
        :raise:
            - QueryEmpty: if there's no conditions defined
            - QueryMissingField: if field() hasn't been set
            - QueryExpressionError: if a expression hasn't been set
        :return:
            - String-type query
        """

        if len(self._query) == 0:
            raise QueryEmpty("At least one condition is required")
        elif self.current_field is None:
            raise QueryMissingField("Logical operator expects a field()")
        elif self.c_oper is None:
            raise QueryExpressionError("field() expects an expression")

        return str().join(self._query)

    def _add_logical_operator(self, operator: Operators.Logical) -> "QueryBuilder":
        """Adds a logical operator in query
        :param operator: logical operator (str)
        :raise:
            - QueryExpressionError: if a expression hasn't been set
        """

        if not self.c_oper:
            raise QueryExpressionError(
                "Logical operators must be preceded by an expression"
            )

        self.current_field = None
        self.c_oper = None

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.l_oper = _f_back.f_code.co_name

        self._query.append(operator)
        return self

    def _add_condition(self, operator, operand, types) -> "QueryBuilder":
        """Appends condition to self._query after performing validation
        :param operator: operator (str)
        :param operand: operand
        :param types: allowed types
        :raise:
            - QueryMissingField: if a field hasn't been set
            - QueryMultipleExpressions: if a condition already has been set
            - QueryTypeError: if the value is of an unexpected type
        """

        if not self.current_field:
            raise QueryMissingField("Conditions requires a field()")

        # elif not type(operand) in types:
        #    caller = inspect.currentframe().f_back.f_code.co_name
        #    raise QueryTypeError(
        #        "Invalid type passed to %s() , expected: %s" % (caller, types)
        #    )

        elif self.c_oper:
            raise QueryMultipleExpressions("Expected logical operator after expression")

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.c_oper = _f_back.f_code.co_name

        self._query.append(
            "%(current_field)s%(operator)s%(operand)s"
            % {
                "current_field": self.current_field,
                "operator": operator,
                "operand": operand,
            }
        )

        return self
