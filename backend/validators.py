import re

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    return True