
class RegistrationResponse:
    SUCCESS = "Success registration"
    ALREADY_EXISTS = ['user with this email already exists.']
    INVALID_EMAIL = ['Enter a valid email address.']


class LoginResponse:
    SUCCESS = "Login Success"
    INVALID = "Invalid Credentials"
    MISSING = "Credentials missing"


class LogoutResponse:
    SUCCESS = "Successfully Logged out"
