from marvel.api.object import Object


class Character(Object):

    def _update(self, **kwargs):
        from marvel.api.url import Url
        self._attribute["urls"] = list(
            map(
                lambda url: Url(url["url"], url["type"]),
                kwargs["urls"]
            )
        )

        from marvel.api.summary import SummaryCollection
        from marvel.api.comic import Comic
        from marvel.api.story import Story
        from marvel.api.event import Event
        from marvel.api.series import Series
        self._attribute["comics"] = SummaryCollection(kwargs["comics"], Comic)
        self._attribute["stories"] = SummaryCollection(
            kwargs["stories"],
            Story
        )
        self._attribute["events"] = SummaryCollection(kwargs["events"], Event)
        self._attribute["series"] = SummaryCollection(
            kwargs["series"],
            Series
        )

        return super()._update(
            ["urls", "comics", "stories", "events", "series"],
            **kwargs
        )

    def attributes(self=None):
        return [
            "id",
            "name",
            "description",
            "modified",
            "resourceURI",
            "urls",
            "thumbnail",
            "comics",
            "stories",
            "events",
            "series"
        ]

    def collection(self=None):
        return CharacterCollection

    def comics(self):
        return self._attribute["comics"]

    def description(self):
        return self._attribute["description"]

    def endpoint(self=None):
        return Object.endpoint(self, "characters")

    def events(self):
        return self._attribute["events"]

    def name(self):
        return self._attribute["name"]

    def series(self):
        return self._attribute["series"]

    def stories(self):
        return self._attribute["stories"]

    def type(self=None):
        return Character

    def urls(self):
        return self._attribute["urls"]


from marvel.api import Api
from marvel.api.object import ObjectCollection


class CharacterCollection(ObjectCollection):

    def __init__(
        self,
        resource="%s%s" % (Api.endpoint(), "characters"),
        data=None
    ):
        from marvel.api.parameter import Parameter
        parameters = {
            "comics": Parameter.comics,
            "events": Parameter.events,
            "modifiedSince": Parameter.modified_since,
            "name": Parameter.name,
            "nameStartsWith": Parameter.name_starts_with,
            "orderBy_modified": Parameter.order_by_modified_ascending,
            "orderBy_-modified": Parameter.order_by_modified_descending,
            "orderBy_name": Parameter.order_by_name_ascending,
            "orderBy_-name": Parameter.order_by_name_descending,
            "series": Parameter.series,
            "stories": Parameter.stories
        }
        super().__init__(resource, data, parameters)

    def collection(self=None):
        return CharacterCollection

    def endpoint(self=None):
        return ObjectCollection.endpoint(self, "characters")

    def type(self=None):
        return Character
