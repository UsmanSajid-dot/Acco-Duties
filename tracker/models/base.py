"""

Base models for the tracker application.

make an empty dictionary to store the models in
loop through every field in the dataclass.
get that fields value as enum and use its value.


"""
from dataclasses import fields
from datetime import date
from enum import Enum
class BaseModel:
    """Base model for all tracker models."""
    special_fields = {}
    def to_dict(self):
        """Convert the model to a dictionary."""
        result = {}
        for field in fields(self):
            value = getattr(self, field.name)
            if isinstance(value, Enum):
                result[field.name] = value.value
            elif isinstance(value, date):
                result[field.name] = value.isoformat()
            else:
                result[field.name] = value
        return result
