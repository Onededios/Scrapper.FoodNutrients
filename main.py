from src.base.logger import Logger
from src.proxies.proxy_bedca import ProxyBedca


LOGGER = Logger()

BEDCA = ProxyBedca(LOGGER)

resp_categories = BEDCA.get_categories()

CATEGORIES = []

for category in resp_categories.get("foodresponse").get("food"):
    ID = int(category["fg_id"])
    SPANISH = category["fg_ori_name"]
    ENGLISH = category["fg_eng_name"]

    CATEGORIES.append(
        {"category_id": ID, "category_spanish": SPANISH, "category_english": ENGLISH}
    )
