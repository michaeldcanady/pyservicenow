from strenum import StrEnum

class RequestItemPriority(StrEnum):
    
    NONE = ""
    CRITICAL = "1"
    HIGH = "2"
    MODERATE = "3"
    LOW = "4"
    
    def __str__(self) -> str:
        
        if self == RequestItemPriority.NONE:
            return "none"
        elif self == RequestItemPriority.CRITICAL:
            return "1 - Critical"
        elif self == RequestItemPriority.HIGH:
            return "2 - High"
        elif self == RequestItemPriority.MODERATE:
            return "3 - Moderate"
        else:
            return "4 - Low"