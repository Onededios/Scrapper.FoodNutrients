import requests
from urllib.parse import urljoin

from src.base.logger import Logger
from typing import Optional, Union
from urllib.parse import urljoin
import requests
import traceback


class Proxy:
    def __init__(self, logger: Logger, base_url: str, headers, cookies=None):
        self._logger = logger
        self.__base_url = base_url
        self.__headers = headers
        self.__cookies = cookies

    def _POST(
        self, endpoint: str, body: Union[dict, str]
    ) -> Optional[requests.Response]:
        try:
            url = urljoin(self.__base_url, endpoint, allow_fragments=True)
            self._logger.info(f"POST request to: {url}")

            response = requests.post(
                url=url,
                json=body if isinstance(body, dict) else None,
                data=body if isinstance(body, str) else None,
                headers=self.__headers,
                cookies=self.__cookies,
                timeout=10,
            )
            response.raise_for_status()
            self._logger.info(f"Response {response.status_code} - {response.reason}")
            return response

        except requests.HTTPError as http_err:
            self._logger.error(
                f"HTTP error occurred: {http_err} - {getattr(http_err.response, 'text', '')}"
            )
        except requests.RequestException as req_err:
            self._logger.error(f"Request error: {req_err}")
            self._logger.debug(traceback.format_exc())

        return None
