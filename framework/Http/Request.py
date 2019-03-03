import requests
import json


class Request:
    def __init__(self):
        pass

    @staticmethod
    def get(url, auth=None):
        return requests.get(url, auth=auth)

    @staticmethod
    def post(url, data):
        if isinstance(data, str):
            return requests.post(url, data=data)
        else:
            return requests.post(url, data=json.dumps(data))
