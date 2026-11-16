from enum import Enum


class FacilityType(Enum):
    '''Shared enum for facility types'''
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"


class Priority(Enum):
    '''Shared enum for priority levels'''
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RepairStatus(Enum):
    '''Shared enum for repair status'''
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
