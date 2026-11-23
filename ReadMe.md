# Acco-Duties
Acco-Duties is a Python application that helps university accommodation students track and manage duties for shared services between students such as shared kitchen and bathroom duties and cleaning rotas, flag for maintenance. The system has both interfaces, GUI and CLI.

## Roadmap
### Phase 1 
- Manage accomodation buildings, floors, rooms and shared facilities like kitchen and bathroom
- Add residents and assign them to rooms
- Make a weekly cleaning rota for every shared facility.
- Mark duties as done or not done
- Assign and view fridge slots
- view dashboard of duties and see who is on duty
- Save all data to a JSON
- Use the app through CLI or GUI
- Flag for maintenance or repairs
### Phase 2
- RentCharge, Payment, RentStatus, rent_service, and rent_view


### Test Cases

Automated tests (pytest, tests/)

[ ] test_models.py: BaseModel round trip (object → dict → JSON → dict → object), including an optional date set to None
[ ] test_json_store.py:
a fresh store when the file is missing
save, then load
IDs count 1, 2, 3, and aren't reused after a delete
insert, get_all, get and delete
[ ] test_repository.py: add sets the ID, list_all returns models, and get and remove work
[ ] test_resident_service.py:
a valid add
an empty name, a bad email and a duplicate email (in any case) are rejected
deleting a missing ID is handled
[ ] conftest.py: a temporary JSON file for each test, so real data is never touched

Manual CLI checks

[ ] Add: success, an empty name, a bad email, a duplicate email
[ ] Show: the empty message, the table alignment, the count
[ ] Delete: a missing ID, the abc input, cancelling with n, no ID reuse
[ ] Data survives a restart
[ ] Navigation: every menu goes back and logs out correctly, and Exit only works from the start screen

Housekeeping linked to testing

[ ] Install pytest and add it to requirements.txt
[ ] Remove the scratch files (test.py, test2.py) once the real tests replace them