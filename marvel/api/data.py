class Data:

    """ Wrapper for data returned after each call to API.
        Can be used to request next items.
    """
    def __init__(self, dict_):
        self.__count = dict_["count"]
        self.__limit = dict_["limit"]
        self.__offset = dict_["offset"]
        self.__raw = dict_["results"]
        self.__total = dict_["total"]

    def __next__(self):
        return next()

    def count(self):
        return int(self.__count)

    def get(self, offset, limit=20):
        if offset >= self.__total:
            raise StopIteration
        if offset + limit > self.__total:
            limit = self.__total - offset
        from urllib.parse import urlencode
        return urlencode({"offset": offset, "limit": limit})

    def from_dict(dict_):
        return Data(
            {
                "count": 1,
                "limit": 20,
                "offset": 0,
                "results": [dict_],
                "total": 1
            }
        )

    def limit(self):
        return int(self.__limit)

    def next(self):
        return Data.get(self, self.__offset + self.__limit, self.__limit)

    def offset(self):
        return int(self.__offset)

    def raw(self):
        return self.__raw

    def total(self):
        return int(self.__total)
