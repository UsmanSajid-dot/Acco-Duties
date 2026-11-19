from tracker.models.base import BaseModel
from tracker.models.enums import Priority
from tracker.storage.json_store import JsonStore
from dataclasses import dataclass
import json
from datetime import date



@dataclass
class Tenant(BaseModel):
    """Model representing a tenant."""

    id: int  
    start_date: date  
    name: str
    email: str
    phone: str
    priority: Priority  
    special_fields = {
        "start_date": lambda x: date.fromisoformat(x),
        "priority": lambda x: Priority(x)}

x = Tenant(id=1, start_date=date(2023, 1, 1), name="John Doe", email="john.doe@example.com", phone="123-456-7890", priority=Priority.HIGH)
print(x.to_dict())
print(json.dumps(x.to_dict()))

print(Tenant.from_dict(x.to_dict()) == x)


store = JsonStore("data/test_store.json")
store.save()
