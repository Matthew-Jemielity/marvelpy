from marvel.api.object import Object


class Creator(Object):

    def _update(self, **kwargs):
        from marvel.api.url import Url
        self._attribute["urls"] = list(
            map(
                lambda url: Url(url["url"], url["type"]),
                kwargs["urls"]
            )
        )

        from marvel.api.summary import SummaryCollection
        from marvel.api.series import Series
        from marvel.api.story import Story
        from marvel.api.comic import Comic
        from marvel.api.event import Event
        self._attribute["series"] = SummaryCollection(kwargs["series"], Series)
        self._attribute["stories"] = SummaryCollection(
            kwargs["stories"],
            Story
        )
        self._attribute["comics"] = SummaryCollection(kwargs["comics"], Comic)
        self._attribute["events"] = SummaryCollection(kwargs["events"], Event)

        return super()._update(
            ["urls", "series", "stories", "comics", "events"],
            kwargs
        )

    def attributes(self=None):
        return [
            "id",
            "firstName",
            "middleName",
            "lastName",
            "suffix",
            "fullName",
            "modified",
            "resourceURI",
            "urls",
            "thumbnail",
            "series",
            "stories",
            "comics",
            "events"
        ]

    def collection(self=None):
        return CreatorCollection

    def comics(self):
        return self._attribute["comics"]

    def endpoint(self=None):
        return Object.endpoint(self, "creators")

    def events(self):
        return self._attribute["events"]

    def first_name(self):
        return self._attribute["firstName"]

    def full_name(self):
        return self._attribute["fullName"]

    def last_name(self):
        return self._attribute["lastName"]

    def middle_name(self):
        return self._attribute["middleName"]

    def series(self):
        return self._attribute["series"]

    def stories(self):
        return self._attribute["stories"]

    def suffix(self):
        return self._attribute["suffix"]

    def type(self=None):
        return Creator

    def urls(self):
        return self._attribute["urls"]


from marvel.api import Api
from marvel.api.object import ObjectCollection


class CreatorCollection(ObjectCollection):
    def __init__(
        self,
        resource="%s%s" % (Api.endpoint(), "creators"),
        data=None
    ):
        from api.parameter import Parameter
        parameters = {
            "comics": Parameter.comics,
            "events": Parameter.events,
            "firstName": Parameter.first_name,
            "firstNameStartsWith": Parameter.first_name_starts_with,
            "lastName": Parameter.last_name,
            "lastNameStartsWith": Parameter.last_name_starts_with,
            "middleName": Parameter.middle_name,
            "middleNameStartsWith": Parameter.middle_name_starts_with,
            "modifiedSince": Parameter.modified_since,
            "nameStartsWith": Parameter.name_starts_with,
            "orderBy_-modified": Parameter.order_by_modified_descending,
            "orderBy_modified": Parameter.order_by_modified_ascending,
            "orderBy_-firstName": Parameter.order_by_first_name_descending,
            "orderBy_-lastName": Parameter.order_by_last_name_descending,
            "orderBy_-middleName": Parameter.order_by_middle_name_descending,
            "orderBy_-suffix": Parameter.order_by_suffix_descending,
            "orderBy_firstName": Parameter.order_by_first_name_ascending,
            "orderBy_lastName": Parameter.order_by_last_name_ascending,
            "orderBy_middleName": Parameter.order_by_middle_name_ascending,
            "orderBy_suffix": Parameter.order_by_suffix_ascending,
            "series": Parameter.series,
            "stories": Parameter.stories,
            "suffix": Parameter.suffix
        }
        super().__init__(resource, data, parameters)

    def collection(self=None):
        return CreatorCollection

    def endpoint(self=None):
        return ObjectCollection.endpoint(self, "creators")

    def type(self=None):
        return Creator
