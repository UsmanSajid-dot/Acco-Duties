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

x = Resident(name="John Doe", email="john.doe@example.com", phone="123-456-7890")

print(x.to_dict())
print(json.dumps(x.to_dict()))
print(Resident.from_dict(x.to_dict()) == x)