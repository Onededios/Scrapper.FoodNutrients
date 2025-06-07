from src.base.logger import Logger
from src.base.proxy import Proxy
from src.base.xml import XML
from src.proxies.models.request_categories import RequestCategories
from xmltodict import parse


class ProxyBedca(Proxy):
    def __init__(self, logger: Logger):
        super().__init__(
            logger,
            "https://www.bedca.net/bdpub/",
            {
                "accept": "*/*",
                "content-type": "text/xml",
                "origin": "https://www.bedca.net",
                "referer": "https://www.bedca.net/bdpub/index.php",
            },
        )

    def get_categories(self):
        parsed = '<?xml version="1.0" encoding="utf-8"?><foodquery><type level="3"/><selection><atribute name="fg_id"/><atribute name="fg_ori_name"/><atribute name="fg_eng_name"/></selection><order ordtype="ASC"><atribute3 name="fg_id"/></order></foodquery>'
        result = self._POST("procquery.php", parsed)
        return parse(result.content)
