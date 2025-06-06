from src.base.proxy import Proxy
from src.base.xml import XML
from src.proxies.models.request_categories import RequestCategories


class ProxyBedca:
    def __init__(self):
        self.__headers = {"Content-Type": "text/xml;charset=UTF-8"}
        self.__proxy = Proxy("https://www.bedca.net/bdpub/", self.__headers)

    def get_categories(self):
        body = {
            "foodquery": {
                "type": {"level": "3"},
                "selection": [
                    {"attribute": {"name": "fg_id"}},
                    {"attribute": {"name": "fg_ori_name"}},
                    {"attribute": {"name": "fg_eng_name"}},
                ],
                "order": {"ordtype": "ASC", "atribute3": {"name": "fg_id"}},
            }
        }
        parser = XML[RequestCategories](body)
        parsed = parser.to_xml()
        result = self.__proxy.POST("procquery.php", parsed)
        return result
