class Url:

    def __init__(self, url, type_="url"):
        self.__url, self.__type = url, type_

    def url(self):
        return self.__url

    def type(self):
        return self.__type
