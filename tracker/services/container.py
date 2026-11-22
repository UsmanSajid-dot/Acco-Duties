from dataclasses import dataclass
from tracker.services.resident_service import ResidentService

@dataclass
class Services:
    """Container for all services in the application."""
    resident: ResidentService