from xml import XML

class File():
    def __init__(self, path):
        self.__path = path
        
    def __read(self):
        with open(self.__path, 'r') as f:
            return f.read()
        
    def XML(self):
        RAW = self.__read()
        return XML(RAW)