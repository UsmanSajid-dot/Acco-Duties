from enum import Enum

class FacilityType(Enum):
    KITCHEN = "Kitchen"
    BATHROOM = "Bathroom"

class PRIORITY(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class REPAIR_STATUS(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
