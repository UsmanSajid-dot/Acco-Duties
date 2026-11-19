from tracker.models.base import BaseModel
from dataclasses import dataclass
import json

@dataclass
class Resident(BaseModel):
    """Model representing a resident."""
  
    name: str
    email: str
    phone: str
    resident_id: int | None = None
