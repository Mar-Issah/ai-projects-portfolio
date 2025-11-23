"""Custom exception classes."""


class APIException(Exception):
    """Base API exception."""

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class OpenAIException(APIException):
    """OpenAI API related exception."""

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code)


class ValidationException(APIException):
    """Validation exception."""

    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message, status_code)


class NotFoundException(APIException):
    """Resource not found exception."""

    def __init__(self, message: str = "Resource not found", status_code: int = 404):
        super().__init__(message, status_code)
