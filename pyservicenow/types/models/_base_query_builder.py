"""Houses Base Query Builder"""

from typing import Union, List, TypeVar, Any
from pyservicenow.types.enums import OrderBy, Operators, RelativeDate

from datetime import datetime

from pyservicenow.types.exceptions import (
    QueryEmpty,
    QueryExpressionError,
    QueryMissingField,
    QueryMultipleExpressions,
)

Q = TypeVar("Q", bound="BaseQueryBuilder")

# https://docs.servicenow.com/en-US/bundle/utah-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html

class BaseQueryBuilder:
    """A class that builds query strings for the ServiceNow API.
    """

    def __init__(self) -> None:
        """Initializes a new query builder.
        """

        super().__init__()

        self._query = []
        self._current_field = None
        self._conditional_operator = None
        self._logical_operator = None

    def field(self: Q, field: str) -> Q:
        """Sets the field to operate on

        Args:
            field (str): The field

        Returns:
            QueryBuilder: The query builder
        """

        self._current_field = field

        return self

    def equals(self: Q, data: Union[str, int]) -> Q:
        """All records in which the field is nothing else but the data value

        Args:
            self (Q): _description_
            data (Union[str, int]): The value the field should equal

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.EQUALS, data)

    def not_equals(self: Q, data: Union[str, int]) -> Q:
        """All records in which the value for the field is anything but the data value

        Args:
            self (Q): _description_
            data (Union[str, int]): The value the field should not equal

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(
            Operators.Comparison.NOTEQUALS, data
        )

    def lesser_or_equal(self: Q, value: Union[str, int, datetime, RelativeDate]) -> Q:
        """All records in which the vlaue in the field is lesser than or equal to the value
        
        For strings it's from "a" to value (value >= "a")

        Args:
            value (Union[str, int, datetime, RelativeDate]): The value for the end constraint

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(
            Operators.Comparison.LESSEROREQUAL, value
        )

    def greater_or_equal(self: Q, value: Union[str, int, datetime, RelativeDate]) -> Q:
        """All records in which the value in the field is greater than or equal to the value.
        
        For strings it's from value to "z" (value <= "z")

        Args:
            value (Union[str, int, datetime, RelativeDate]): The value for the beginning constraint

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(
            Operators.Comparison.GREATEROREQUAL, value
        )

    def is_between(self: Q, value1: Union[str, int], value2: Union[str, int]) -> Q:
        """All records in which the field is between value1 and value2. For string fields it is the first letter.

        Args:
            value1 (Union[str, int]): The beginning of the range
            value2 (Union[str, int]): The end of the range.

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.BETWEEN, f"{value1}@{value2}")

    def is_same(self: Q, field: str) -> Q:
        """All records in which there exist matching values for the first and second fields.

        Args:
            field (str): The secondary field

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.ISSAME, field)

    def is_different(self: Q, field: str) -> Q:
        """All records in which there exist differing values for the first and second fields.

        Args:
            field (str): The secondary field

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.ISDIFFERENT, field)

    def is_empty(self: Q) -> Q:
        """All records in which the field has no value.

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.ISEMPTY, None)

    def is_not_empty(self: Q) -> Q:
        """All records in which there is any value in the field

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.ISNOTEMPTY, None)

    def is_anything(self: Q) -> Q:
        """All records in which the field is one of the following:
        - any value
        - empty
        - NULL

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        return self._add_condition(Operators.Comparison.ISANYTHING, None)

    def order_by(self: Q, direction: OrderBy, field = None) -> Q:
        """Sets the order by direction

        Args:
            direction (OrderBy): Direction to order results by

        Returns:
            QueryBuilder: The current QueryBuilder object
        """
        
        if field is None:
            field = self._current_field

        _order_by_string = f"{direction}{field}"

        self._query.append(_order_by_string)
        self._conditional_operator = "order_by"

        return self

    def is_one_of(self: Q, data: List[Union[str, int]]) -> Q:
        return self._add_condition(
            Operators.Comparison.IN, ",".join(map(str, data))
        )

    def is_not_one_of(self: Q, data: List[Union[str, int]]) -> Q:
        return self._add_condition(
            Operators.Comparison.NOTIN, ",".join(map(str, data))
        )


    def starts_with(self: Q, data: str) -> Q:
        return self._add_condition(Operators.Comparison.STARTSWITH, data)

    def ends_with(self: Q, data: str) -> Q:
        
        return self._add_condition(Operators.Comparison.ENDSWITH, data)

    def contains(self: Q, contains: str) -> Q:

        return self._add_condition(Operators.Comparison.LIKE, contains)

    def does_not_contains(self: Q, does_not_contains: str) -> Q:

        return self._add_condition(
            Operators.Comparison.NOTLIKE, does_not_contains
        )

    @property
    def AND(self: Q) -> Q:

        return self._add_logical_operator(Operators.Logical.AND)

    @property
    def OR(self: Q) -> Q:

        return self._add_logical_operator(Operators.Logical.OR)

    @property
    def NQ(self: Q) -> Q:

        return self._add_logical_operator(Operators.Logical.NEWQUERY)

    @property
    def EQ(self: Q) -> Q:
 
        return self._add_logical_operator(Operators.Logical.ENDQUERY)
    
    def __str__(self) -> str:
        """String representation of the query object
        :raise:
            - QueryEmpty: if there's no conditions defined
            - QueryExpressionError: if a expression hasn't been set
        :return:
            - String-type query
        """

        if len(self._query) == 0:
            raise QueryEmpty("At least one condition is required")
        elif self._conditional_operator is None:
            raise QueryExpressionError("field() expects an expression")
        
        query_string = ""
        
        for fragment in self._query:
            
            if isinstance(fragment, tuple):
                fragment = "".join(fragment)
            query_string += fragment

        return query_string

    def _add_logical_operator(self: Q, operator: Operators.Logical) -> Q:
        """Adds a logical operator in query
        :param operator: logical operator (str)
        :raise:
            - QueryExpressionError: if a expression hasn't been set
        """
        
        if not self._conditional_operator and self._query[-1] != Operators.Logical.ENDQUERY:
            raise QueryExpressionError(
                "Logical operators must be preceded by an expression"
            )

        self._current_field = None
        self._conditional_operator = None

        self._logical_operator = operator

        self._query.append(operator)
        return self

    def _add_condition(
        self: Q, operator: Operators.Comparison, operand: Any) -> Q:
        """Appends condition to self._query after performing validation
        :param operator: operator (str)
        :param operand: operand
        :param types: allowed types
        :raise:
            - QueryMissingField: if a field hasn't been set
            - QueryMultipleExpressions: if a condition already has been set
        """

        if not self._current_field:
            raise QueryMissingField("Conditions require a field()")

        if self._conditional_operator:
            raise QueryMultipleExpressions("Expected logical operator after expression")

        self._conditional_operator = operator
        
        if operand is None:
            operand = ""
            
        if isinstance(operand, RelativeDate):
            operand = operand.to_javascript()
        
        if isinstance(operand, datetime):
            operand = self._datetime_to_javascript(operand)
            
            
        # f"{self._current_field}{operator}{operand}"

        self._query.append((self._current_field, operator, operand, ))

        return self
    
    def _datetime_to_javascript(self, date: datetime) -> str:
        """Converts datetime to the JavaScript version
        
        Args:
            date (datetime): The datetime object to convert
            
        Returns:
            str: The JavaScript version of the datetime object
        """
        
        date_str = date.strftime("%Y-%m-%d")
        time_str = date.strftime("%H:%M:%S")
        
        return f"javascript:gs.dateGenerate('{date_str}','{time_str}')"