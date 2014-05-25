from marvel.api.object import Object
class Event( Object ):
    def _update( self, **kwargs ):
        from marvel.api.url import Url
        self._attribute[ "urls" ] = list( map( lambda url: Url( url[ "url" ], url[ "type" ] ), kwargs[ "urls" ] ) )
        from marvel.api.summary import Summary
        self._attribute[ "next" ], self._attribute[ "previous" ] = Summary( kwargs[ "next" ], Event ), Summary( kwargs[ "previous" ], Event )
        from marvel.api.summary import SummaryCollection
        from marvel.api.comic import Comic
        from marvel.api.story import Story
        from marvel.api.series import Series
        from marvel.api.character import Character
        from marvel.api.creator import Creator
        self._attribute[ "comics" ], self._attribute[ "stories" ], self._attribute[ "series" ], self._attribute[ "characters" ], self._attribute[ "creators" ] = SummaryCollection( kwargs[ "comics" ], Comic ), SummaryCollection( kwargs[ "stories" ], Story ), SummaryCollection( kwargs[ "series" ], Series ), SummaryCollection( kwargs[ "characters" ], Character ), SummaryCollection( kwargs[ "creators" ], Creator )
        return super()._update( [ "urls", "comics", "stories", "series", "characters", "creators", "next", "previous" ], kwargs )
    def attributes( self = None ): return [ "id", "title", "description", "resourceURI", "urls", "modified", "start", "end", "thumbnail", "comics", "stories", "series", "characters", "creators", "next", "previous" ]
    def characters( self ): return self._attribute[ "characters" ]
    def collection( self = None ): return EventCollection
    def comics( self ): return self._attribute[ "comics" ]
    def creators( self ): return self._attribute[ "creators" ]
    def description( self ): return self._attribute[ "description" ]
    def end( self ): return self._attribute[ "end" ]
    def endpoint( self = None ): return Object.endpoint( self, "events" )
    def next( self ): return self._attribute[ "next" ]
    def previous( self ): return self._attribute[ "previous" ]
    def series( self ): return self._attribute[ "series" ]
    def start( self ): return self._attribute[ "start" ]
    def stories( self ): return self._attribute[ "stories" ]
    def title( self ): return self._attriubte[ "title" ]
    def type( self = None ): return Event
    def urls( self ): return self._attribute[ "urls" ]

from marvel.api import Api
from marvel.api.object import ObjectCollection
class EventCollection( ObjectCollection ):
    def __init__( self, resource = "%s%s" % ( Api.endpoint(), "events" ), data = None ):
        from api.parameter import Parameter
        parameters = {
            "characters" : Parameter.characters,
            "comics" : Parameter.comics,
            "creators" : Parameter.creators,
            "modifiedSince" : Parameter.modified_since,
            "name" : Parameter.name,
            "nameStartsWith" : Parameter.name_starts_with,
            "orderBy_-modified" : Parameter.order_by_modified_descending,
            "orderBy_-name" : Parameter.order_by_name_descending,
            "orderBy_-startDate" : Parameter.order_by_start_date_descending,
            "orderBy_modified" : Parameter.order_by_modified_ascending,
            "orderBy_name" : Parameter.order_by_name_ascending,
            "orderBy_startDate" : Parameter.order_by_start_date_ascending,
            "series" : Parameter.series,
            "stories" : Parameter.stories
        }
        super().__init__( resource, data, parameters )
    def collection( self = None ): return EventCollection
    def endpoint( self = None ): return ObjectCollection.endpoint( self, "events" )
    def type( self = None ): return Event

