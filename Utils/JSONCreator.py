import json

def getJsonFromArray(array):
        data = {
            "data": array
        }
        return json.dumps(data)