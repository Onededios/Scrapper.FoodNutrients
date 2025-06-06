import requests
from urllib.parse import urljoin


class Proxy:
    def __init__(self, base_url, headers):
        self.__base_url = base_url
        self.__base_headers = headers

    def POST(self, endpoint, body):
        URL = urljoin(self.__base_url, endpoint, allow_fragments=True)
        response = requests.post(url=URL, json=body, headers=self.__base_headers)
        response.raise_for_status()
        return response
