class Text:

    def __init__(self, text, language="EN", type_="text"):
        self.__text, self.__language, self.__type = text, language, type_

    def text(self):
        return self.__text

    def language(self):
        return self.__language

    def type(self):
        return self.__type
