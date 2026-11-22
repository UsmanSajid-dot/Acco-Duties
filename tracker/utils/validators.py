from tracker.utils.exceptions import ValidationError

def is_valid_email(email):
    """Check if the provided email is valid."""
    # Basic validation for email format
    if "@" not in email or "." not in email:
        raise ValidationError(f"Invalid email format: {email}")
    return True

