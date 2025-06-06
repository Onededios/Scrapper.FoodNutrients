import xmltodict


class XML[T]():
    def __init__(self, raw):
        self.__content = raw

    def to_xml(self) -> str:
        return xmltodict.unparse(self.__content, pretty=True)

    def from_xml(self) -> T:
        parsed = xmltodict.parse(self.__content)
        return T(**parsed)
