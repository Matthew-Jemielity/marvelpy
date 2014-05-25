from marvel.api.object import Object
class Series( Object ):
    def _update( self, **kwargs ):
        self._attribute[ "startYear" ], self._attribute[ "endYear" ] = int( kwargs[ "startYear" ] ), int( kwargs[ "endYear" ] )
        from marvel.api.url import Url
        self._attribute[ "urls" ] = list( map( lambda url: Url( url[ "url" ], url[ "type" ] ), kwargs[ "urls" ] ) )
        from marvel.api.summary import Summary
        self._attribute[ "next" ], self._attribute[ "previous" ] = Summary( kwargs[ "next" ], Series ), Summary( kwargs[ "previous" ], Series )
        from marvel.api.summary import SummaryCollection
        from marvel.api.comic import Comic
        from marvel.api.story import Story
        from marvel.api.event import Event
        from marvel.api.character import Character
        from marvel.api.creator import Creator
        self._attribute[ "comics" ], self._attribute[ "stories" ], self._attribute[ "events" ], self._attribute[ "characters" ], self._attribute[ "creators" ] = SummaryCollection( kwargs[ "comics" ], Comic ), SummaryCollection( kwargs[ "stories" ], Story ), SummaryCollection( kwargs[ "events" ], Event ), SummaryCollection( kwargs[ "characters" ], Character ), SummaryCollection( kwargs[ "creators" ], Creator )
        return super()._update( [ "urls", "startYear", "endYear", "comics", "stories", "events", "characters", "creators", "next", "previous" ], kwargs )
    def attributes( self = None ): return [ "id", "title", "description", "resourceURI", "urls", "startYear", "endYear", "rating", "modified", "thumbnail", "comics", "stories", "events", "characters", "creators", "next", "previous" ]
    def characters( self ): return self._attribute[ "characters" ]
    def creators( self ): return self._attribute[ "creators" ]
    def collection( self = None ): return SeriesCollection
    def comics( self ): return self._attribute[ "comics" ]
    def description( self ): return self._attribute[ "description" ]
    def end_year( self ): return self._attribute[ "endYear" ]
    def endpoint( self = None ): return Object.endpoint( self, "series" )
    def events( self ): return self._attribute[ "events" ]
    def next( self ): return self._attribute[ "next" ]
    def previous( self ): return self._attribute[ "previous" ]
    def rating( self ): return self._attribute[ "rating" ]
    def start_year( self ): return self._attribute[ "startYear" ]
    def stories( self ): return self._attribute[ "stories" ]
    def title( self ): return self._attribute[ "title" ]
    def type( self = None ): return Series
    def urls( self ): return self._attribute[ "urls" ]

from marvel.api import Api
from marvel.api.object import ObjectCollection
class SeriesCollection( ObjectCollection ):
    def __init__( self, resource = "%s%s" % ( Api.endpoint(), "series" ), data = None ):
        from api.parameter import Parameter
        parameters = {
            "characters" : Parameter.characters,
            "comics" : Parameter.comics,
            "creators" : Parameter.creators,
            "events" : Parameter.events,
            "modifiedSince" : Parameter.modified_since,
            "orderBy_-modified" : Parameter.order_by_modified_descending,
            "orderBy_-startYear" : Parameter.order_by_start_year_descending,
            "orderBy_-title" : Parameter.order_by_title_descending,
            "orderBy_modified" : Parameter.order_by_modified_ascending,
            "orderBy_startYear" : Parameter.order_by_start_year_ascending,
            "orderBy_title" : Parameter.order_by_title_ascending,
            "seriesType_collection" : Parameter.series_type_collection,
            "seriesType_limited" : Parameter.series_type_limited,
            "seriesType_one_shot" : Parameter.series_type_one_shot,
            "seriesType_ongoing" : Parameter.series_type_ongoing,
            "startYear" : Parameter.start_year,
            "stories" : Parameter.stories,
            "title" : Parameter.title,
            "titleStartsWith" : Parameter.title_starts_with
        }
        super().__init__( resource, data, parameters )
    def collection( self = None ): return SeriesCollection
    def endpoint( self = None ): return ObjectCollection.endpoint( self, "series" )
    def type( self = None ): return Series

