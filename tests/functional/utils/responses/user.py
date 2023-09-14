class RegistrationResponse:
    SUCCESS = "Success registration"
    ALREADY_EXISTS = "user with this email already exists."
    INVALID_EMAIL = "Enter a valid email address."
    PASSWORD_NUMERIC = "This password is entirely numeric."
    PASSWORD_LENGTH = (
        "This password is too short. It must contain at least 8 characters."
    )


class LoginResponse:
    SUCCESS = "Login Success"
    INVALID = "Invalid Credentials"
    MISSING = "Credentials missing"


class LogoutResponse:
    SUCCESS = "Successfully Logged out"
