import string
import json

from model import APIStatus


def buildResponse(status: APIStatus, data=None, message=None):
    response = {
        "status": status.description,
        "code": status.code
    }

    if status.is_failure and message:
        response["message"] = message
    elif status.is_success and data is not None:
        response["data"] = data

    return response