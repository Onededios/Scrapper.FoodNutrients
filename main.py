from src.proxies.proxy_bedca import ProxyBedca


BEDCA = ProxyBedca()

res = BEDCA.get_categories()
print(res.content)
