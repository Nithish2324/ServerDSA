from enum import Enum


class APIStatus(Enum):
    SUCCESS = (200, "Success")

    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORIZED = (401, "Unauthorized")
    FORBIDDEN = (403, "Forbidden")
    NOT_FOUND = (404, "Not Found")
    VALIDATION_ERROR = (422, "Validation Error")
    RATE_LIMITED = (429, "Rate Limited")
    SERVER_ERROR = (500, "Internal Server Error")
    TIMEOUT = (504, "Gateway Timeout")

    @property
    def code(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

    @property
    def is_success(self):
        return self == APIStatus.SUCCESS

    @property
    def is_failure(self):
        return self != APIStatus.SUCCESS