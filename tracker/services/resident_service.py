from tracker.utils.exceptions import ValidationError
from tracker.utils.validators import is_valid_email


class ResidentService:
    def __init__(self, repo):
        self.repository = repo

    def create_resident(self, name, email, phone):
        # Validate the email
        if not is_valid_email(email):
            raise ValidationError(f"Invalid email format: {email}")

        # Create a new Resident instance
        new_resident = self.repository.model_cls(name=name, email=email, phone=phone)

        # Save the new resident using the repository
        saved_resident = self.repository.add(new_resident)
        return saved_resident

    def list_residents(self):
        return self.repository.list_all()
    