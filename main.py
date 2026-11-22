from interfaces.cli.app import run
from tracker.storage.json_store import JsonStore
from tracker.storage.repository import Repository
from tracker.models.resident import Resident
from tracker.services.container import Services
from tracker.services.resident_service import ResidentService

if __name__ == "__main__":
    store = JsonStore("data/test_store.json")
    resident_repo = Repository(store, "resident", Resident)
    resident_service = ResidentService(resident_repo)
    services = Services(resident=resident_service)


    run(services)