from marvel.api import Api


class Object(Api):

    """ Base class for API entities.
        It contains "abstract" methods that must be implemented by descendants.
    """
    def _update(self, omit=[], **kwargs):
        omit.append("thumbnail")
        for key in list(
            filter(
                lambda key: key not in omit,
                kwargs.keys()
            )
        ):
            self._attribute[key] = kwargs[key]
        from marvel.api.image import Image
        self._attribute["thumbnail"] = None if kwargs[
                "thumbnail"
            ] is None else Image(
            kwargs["thumbnail"]["path"],
            kwargs["thumbnail"]["extension"]
        )
        return self

    def __init__(self, id_, data=None):
        super().__init__()
        for element in self.attributes():
            self._attribute[element] = None
        self._attribute["id"] = int(id_)
        self._attribute["resourceURI"] = "%s/%d" % (
            self.type().endpoint(),
            int(id_)
        )
        if data is not None:
            self._update(
                **dict(
                    zip(
                        self.attributes(),
                        list(
                            map(
                                lambda attribute: data.raw()[0][attribute],
                                self.attributes()
                            )
                        )
                    )
                )
            )  # will overwrite id, resourceURI

    def attributes(self=None):
        return ["id", "modified", "resourceURI", "thumbnail"]

    def call(self, data="", etag=None):
        called = super().call(self.endpoint(), data, etag)
        return called._update(
            **dict(
                zip(
                    called.attributes(),
                    list(
                        map(
                            lambda attribute: called.data().raw()[0][
                                attribute
                            ],
                            called.attributes()
                        )
                    )
                )
            )
        )

    def collection(self=None):
        return ObjectCollection

    def endpoint(self=None, type_=None):
        if type_ is None:
            raise NotImplementedError
        return "%s%s" % (
            Api.endpoint(),
            type_
        ) if self is None else self.resource()

    def id(self):
        return self._attribute["id"]

    def modified(self):
        return self._attribute["modified"]

    def resource(self):
        return self._attribute["resourceURI"]

    def thumbnail(self):
        return self._attribute["thumbnail"]

    def type(self=None):
        return Object


class ObjectCollection(Api):

    def _update(self, data):
        from marvel.api.data import Data
        self.__items = list(
            map(
                lambda dict_: self.type()(
                    int(dict_["id"]),
                    Data.from_dict(dict_)
                ),
                data.raw()
            )
        )
        return self

    def __init__(self, resource, data=None, parameters=[]):
        super().__init__()
        self.__resource = resource
        self.__items = []
        self.__parameters = parameters
        from marvel.api.parameter import Parameter
        self.__parameter = Parameter()
        if data is not None:
            ObjectCollection._update(self, data)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def call(self, data="", etag=None):
        parameters = self.__parameter.get()
        called = super().call(
            self.endpoint(),
            "%s%s%s" % (
                parameters,
                "" if (parameters is "" and data is "") else "&",
                data
            ),
            etag
        )
        return ObjectCollection._update(called, called.data())

    def collection(self=None):
        return ObjectCollection

    def endpoint(self=None, type_=None):
        if type_ is None:
            raise NotImplementedError
        return "%s%s" % (
            Api.endpoint(),
            type_
        ) if self is None else self.resource()

    def items(self):
        return self.__items

    def next(self):
        try:
            return self.call(self.data().next())
        except AttributeError:
            return self.call()

    def parameter(self, key, *args):
        return self.__parameter.add(self.__parameters[key](*args))

    def resource(self):
        return self.__resource

    def type(self=None):
        return Object
