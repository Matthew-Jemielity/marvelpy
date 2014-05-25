from marvel.api.object import Object
class Comic( Object ):
    def _update( self, **kwargs ):
        from marvel.api.series import Series
        from marvel.api.summary import Summary
        self._attribute[ "series" ] = Summary( kwargs[ "series" ], Series )
        from marvel.api.text import Text
        self._attribute[ "textObjects" ] = list( map( lambda text: Text( text[ "text" ], text[ "language" ], text[ "type" ] ), kwargs[ "textObjects" ] ) )
        from marvel.api.url import Url
        self._attribute[ "urls" ] = list( map( lambda url: Url( url[ "url" ], url[ "type" ] ), kwargs[ "urls" ] ) )
        self._attribute[ "variants" ] = list( map( lambda variant: Summary( variant, Comic ), kwargs[ "variants" ] ) )
        self._attribute[ "collections" ] = list( map( lambda collection: Summary( collection, Comic ), kwargs[ "collections" ] ) )
        self._attribute[ "collectedIssues" ] = list( map( lambda issue: Summary( issue, Comic ), kwargs[ "collectedIssues" ] ) )
        self._attribute[ "dates" ] = list( map( lambda date: ComicDate( date[ "type" ], date[ "date" ] ), kwargs[ "dates" ] ) )
        self._attribute[ "prices" ] = list( map( lambda price: ComicPrice( price[ "type" ], price[ "price" ] ), kwargs[ "prices" ] ) )
        from marvel.api.image import Image
        self._attribute[ "images" ] = list( map( lambda image: Image( image[ "path" ], image[ "extension" ] ), kwargs[ "images" ] ) )
        from marvel.api.summary import SummaryCollection
        from marvel.api.creator import Creator
        from marvel.api.character import Character
        from marvel.api.story import Story
        from marvel.api.event import Event
        self._attribute[ "creators" ], self._attribute[ "characters" ], self._attribute[ "stories" ], self._attribute[ "events" ] = SummaryCollection( kwargs[ "creators" ], Creator ), SummaryCollection( kwargs[ "characters" ], Character ), SummaryCollection( kwargs[ "stories" ], Story ), SummaryCollection( kwargs[ "events" ], Event )
        return super()._update( [ "series", "textObjects", "urls", "variants", "collections", "collectedIssues", "dates", "prices", "images", "creators", "characters", "stories", "events" ], **kwargs )
    def attributes( self = None ): return [ "id", "digitalId", "title", "issueNumber", "variantDescription", "description", "modified", "isbn", "upc", "diamondCode", "ean", "issn", "format", "pageCount", "textObjects", "resourceURI", "urls", "series", "variants", "collections", "collectedIssues", "dates", "prices", "thumbnail", "images", "creators", "characters", "stories", "events" ]
    def characters( self ): return self._attribute[ "characters" ]
    def collected_issues( self ): return self._attribute[ "collectedIssues" ]
    def collection( self = None ): return ComicCollection
    def collections( self ): return self._attribute[ "collections" ]
    def creators( self ): self._attribute[ "creators" ]
    def dates( self ): return self._attribute[ "dates" ]
    def description( self ): return self._attribute[ "description" ]
    def diamond_code( self ): return self._attribute[ "diamondCode" ]
    def digital_id( self ): return self._attribute[ "digitalId" ]
    def ean( self ): return self._attribute[ "ean" ]
    def endpoint( self = None ): return Object.endpoint( self, "comics" )
    def events( self ): return self._attribute[ "events" ]
    def format( self ): return self._attribute[ "format" ]
    def images( self ): return self._attribute[ "images" ]
    def isbn( self ): return self._attribute[ "isbn" ]
    def issn( self ): return self._attribute[ "issn" ]
    def issue_number( self ): return self._attribute[ "issueNumber" ]
    def page_count( self ): return self._attribute[ "pageCount" ]
    def prices( self ): return self._attribute[ "prices" ]
    def series( self ): return self._attribute[ "series" ]
    def stories( self ): return self._attribute[ "stories" ]
    def texts( self ): return self._attribute[ "textObjects" ]
    def title( self ): return self._attribute[ "title" ]
    def type( self = None ): return Comic
    def upc( self ): return self._attribute[ "upc" ]
    def urls( self ): return self._attribute[ "urls" ]
    def variant_description( self ): return self._attribute[ "variantDescription" ]
    def variants( self ): return self._attribute[ "variants" ]

from marvel.api import Api
from marvel.api.object import ObjectCollection
class ComicCollection( ObjectCollection ):
    def __init__( self, resource = "%s%s" % ( Api.endpoint(), "comics" ), data = None ):
        from marvel.api.parameter import Parameter
        parameters = {
            "characters" : Parameter.characters,
            "collaborators" : Parameter.collaborators,
            "contains_comic" : Parameter.contains_comic,
            "creators" : Parameter.creators,
            "dateDescriptor_lastWeek" : Parameter.date_last_week,
            "dateDescriptor_nextWeek" : Parameter.date_next_week,
            "dateRange" : Parameter.date_range,
            "dateDescriptor_thisMonth" : Parameter.date_this_month,
            "dateDescriptor_thisWeek" : Parameter.date_this_week,
            "diamondCode" : Parameter.diamond_code,
            "digitalId" : Parameter.digital_id,
            "ean" : Parameter.ean,
            "events" : Parameter.events,
            "format_comic" : Parameter.format_comic,
            "format_digest" : Parameter.format_digest,
            "format_digital_comic" : Parameter.format_digital_comic,
            "format_graphic_novel" : Parameter.format_graphic_novel,
            "format_hardcover" : Parameter.format_hardcover,
            "format_infinite_comic" : Parameter.format_infinite_comic,
            "format_magazine" : Parameter.format_magazine,
            "format_trade_paperback" : Parameter.format_trade_paperback,
            "formatType_collection" : Parameter.format_type_collection,
            "formatType_comic" : Parameter.format_type_comic,
            "hasDigitalIssue" : Parameter.has_digital_issue,
            "isbn" : Parameter.isbn,
            "issn" : Parameter.issn,
            "modifiedSince" : Parameter.modified_since,
            "noVariants" : Parameter.no_variants,
            "orderBy_focDate" : Parameter.order_by_FOC_date_ascending,
            "orderBy_-focDate" : Parameter.order_by_FOC_date_descending,
            "orderBy_issueNumber" : Parameter.order_by_issue_ascending,
            "orderBy_-issueNumber" : Parameter.order_by_issue_descending,
            "orderBy_modified" : Parameter.order_by_modified_ascending,
            "orderBy_-modified" : Parameter.order_by_modified_descending,
            "orderBy_onsaleDate" : Parameter.order_by_sale_date_ascending,
            "orderBy_-onsaleDate" : Parameter.order_by_sale_date_descending,
            "orderBy_title" : Parameter.order_by_title_ascending,
            "orderBy_-title" : Parameter.order_by_title_descending,
            "series" : Parameter.series,
            "stories" : Parameter.stories,
            "sharedAppearances" : Parameter.teamups,
            "title" : Parameter.title,
            "titleStartsWith" : Parameter.title_starts_with,
            "upc" : Parameter.upc
        }
        super().__init__( resource, data, parameters )
    def collection( self = None ): return ComicCollection
    def endpoint( self = None ): return ObjectCollection.endpoint( self, "comics" )
    def type( self = None ): return Comic

class ComicDate( object ):
    def __init__( self, type_, date ): self.__type, self.__date = type_, date
    def type( self ): return self.__type
    def date( self ): return self.__date

class ComicPrice( object ):
    def __init__( self, type_, price ): self.__type, self.__price = type_, price
    def type( self ): return self.__type
    def price( self ): return self.__price

