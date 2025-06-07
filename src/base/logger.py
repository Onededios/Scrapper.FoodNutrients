import logging
import sys


class Logger:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(
            logging.Formatter(f"%(asctime)s - %(levelname)s - %(message)s")
        )

        self.__logger.addHandler(console_handler)

    def debug(self, msg: str, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)
