from strenum import StrEnum

class RelativeDate(StrEnum):
    TODAY = "Today"
    YESTERDAY = "Yesterday"
    TOMORROW = "Tomorrow"
    THIS_WEEK = "This week"
    LAST_WEEK = "Last week"
    NEXT_WEEK = "Next week"
    THIS_MONTH = "This month"
    LAST_MONTH = "Last month"
    NEXT_MONTH = "Next month"
    LAST_3_MONTHS = "Last 3 months"
    LAST_6_MONTHS = "Last 6 months"
    LAST_9_MONTHS = "Last 9 months"
    LAST_12_MONTHS = "Last 12 months"
    THIS_QUARTER = "This quarter"
    LAST_QUARTER = "Last quarter"
    NEXT_QUARTER = "Next quarter"
    LAST_2_QUARTERS = "Last 2 quarters"
    NEXT_2_QUARTERS = "Next 2 quarters"
    THIS_YEAR = "This year"
    NEXT_YEAR = "Next year"

    def to_javascript(self) -> str:
        """Converts RelativeDate to the JavaScript version
        
        Returns:
            str: The JavaScript version
        """
        
        return {
            RelativeDate.TODAY: "javascript:gs.daysAgoStart(0)",
            RelativeDate.YESTERDAY: "javascript:gs.daysAgoStart(1)",
            RelativeDate.TOMORROW: "javascript:gs.daysAgoEnd(-1)",
            RelativeDate.THIS_WEEK: "javascript:gs.beginningOfThisWeek()",
            RelativeDate.LAST_WEEK: "javascript:gs.beginningOfLastWeek()",
            RelativeDate.NEXT_WEEK: "javascript:gs.endOfNextWeek()",
            RelativeDate.THIS_MONTH: "javascript:gs.beginningOfThisMonth()",
            RelativeDate.LAST_MONTH: "javascript:gs.beginningOfLastMonth()",
            RelativeDate.NEXT_MONTH: "javascript:gs.endOfNextMonth()",
            RelativeDate.LAST_3_MONTHS: "javascript:gs.beginningOfLast3Months()",
            RelativeDate.LAST_6_MONTHS: "javascript:gs.beginningOfLast6Months()",
            RelativeDate.LAST_9_MONTHS: "javascript:gs.beginningOfLast9Months()",
            RelativeDate.LAST_12_MONTHS: "javascript:gs.beginningOfLast12Months()",
            RelativeDate.THIS_QUARTER: "javascript:gs.beginningOfThisQuarter()",
            RelativeDate.LAST_QUARTER: "javascript:gs.beginningOfLastQuarter()",
            RelativeDate.NEXT_QUARTER: "javascript:gs.endOfNextQuarter()",
            RelativeDate.LAST_2_QUARTERS: "javascript:gs.beginningOfLast2Quarters()",
            RelativeDate.NEXT_2_QUARTERS: "javascript:gs.endOfNext2Quarters()",
            RelativeDate.THIS_YEAR: "javascript:gs.beginningOfThisYear()",
            RelativeDate.NEXT_YEAR: "javascript:gs.endOfNextYear()",
        }[self]