from marvel.api.object import Object
class Story( Object ):
    def _update( self, **kwargs ):
        from marvel.api.summary import Summary
        from marvel.api.comic import Comic
        self._attribute[ "originalIssue" ] = Summary( kwargs[ "originalIssue" ], Comic )
        from marvel.api.summary import SummaryCollection
        from marvel.api.series import Series
        from marvel.api.event import Event
        from marvel.api.character import Character
        from marvel.api.creator import Creator
        self._attribute[ "comics" ], self._attribute[ "series" ], self._attribute[ "events" ], self._attribute[ "characters" ], self._attribute[ "creators" ] = SummaryCollection( kwargs[ "comics" ], Comic ), SummaryCollection( kwargs[ "series" ], Series ), SummaryCollection( kwargs[ "events" ], Event ), SummaryCollection( kwargs[ "characters" ], Character ), SummaryCollection( kwargs[ "creators" ], Creator )
        return super()._update( [ "comics", "series", "events", "characters", "creators", "originalIssue" ], kwargs )
    def attributes( self = None ): return [ "id", "title", "description", "resourceURI", "type", "modified", "thumbnail", "comics", "series", "events", "characters", "creators", "originalIssue" ]
    def collection( self = None ): return StoryCollection
    def characters( self ): return self._attribute[ "characters" ]
    def comics( self ): return self._attribute[ "comics" ]
    def creators( self ): return self._attribute[ "creators" ]
    def description( self ): return self._attribute[ "description" ]
    def endpoint( self = None ): return Object.endpoint( self, "stories" )
    def events( self ): return self._attribute[ "events" ]
    def original_issue( self ): return self._attribute[ "originalIssue" ]
    def series( self ): return self._attribute[ "series" ]
    def story_type( self ): return self._attribute[ "type" ]
    def title( self ): return self._attribute[ "title" ]
    def type( self = None ): return Story

from marvel.api import Api
from marvel.api.object import ObjectCollection
class StoryCollection( ObjectCollection ):
    def __init__( self, resource = "%s%s" % ( Api.endpoint(), "stories" ), data = None ):
        from api.parameter import Parameter
        parameters = {
            "characters" : Parameters.characters,
            "comics" : Parameter.comics,
            "creators" : Parameter.creators,
            "events" : Parameter.events,
            "modifiedSince" : Parameter.modified_since,
            "orderBy_-id" : Parameters.order_by_id_descending,
            "orderBy_-modified" : Parameter.order_by_modified_descending,
            "orderBy_id" : Parameters.order_by_id_ascending,
            "orderBy_modified" : Parameter.order_by_modified_ascending,
            "series" : Parameter.series
        }
        super().__init__( resource, data, parameters )
    def collection( self = None ): return StoryCollection
    def endpoint( self = None ): return ObjectCollection.endpoint( self, "stories" )
    def type( self = None ): return Story

