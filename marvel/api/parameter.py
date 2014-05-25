class Parameter:
    def __init__( self, parameters = [ ] ):
        self.__parameters = [ ]
        for parameter in parameters: self.add( parameter )
    def add( self, parameter ):
        # parameter must be { "key" : "value" }
        try:
            if list( parameter.keys() )[0] is not str( list( parameter_.keys() )[0] ): raise ParameterError
            if list( parameter.values() )[0] is not str( list( parameter_.values() )[0] ): raise ParameterError
        except ( AttributeError, IndexError, TypeError ): raise ParameterError
        self.__parameters.append( parameter )
    def get( self ):
        from urllib.parse import urlencode
        # from list of single-element dicts to a concatenated dict, urlencoded into string
        return urlencode( dict( list( map( lambda key, value: ( key, value ), list( map( lambda parameter: list( parameter.keys() ) [ 0 ], self.__parameters) ), list( map( lambda parameter: list( parameter.values() ) [ 0 ], self.__parameters ) ) ) ) ) )
    def characters( list_ ): return { "characters" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def collaborators( list_ ): return { "collaborators" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def comics( list_ ): return { "comics" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def contains_comic(): return { "contains" : "comic" }
    def contains_digest(): return { "contains" : "digest" }
    def contains_digital_comic(): return { "contains" : "digital comic" }
    def contains_graphic_novel(): return { "contains" : "graphic novel" }
    def contains_hardcover(): return { "contains" : "hardcover" }
    def contains_infinite_comic(): return { "contains" : "infinite comic" }
    def contains_magazine(): return { "contains" : "magazine" }
    def contains_trade_paperback(): return { "contains" : "trade paperback" }
    def creators( list_ ): return { "creators" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def date_last_week(): return { "dateDescriptor" : "lastWeek" }
    def date_next_week(): return { "dateDescriptor" : "nextWeek" }
    def date_range( from_, to ): return { "dateRange" : str( from_ ) + "," + str( to_ ) }
    def date_this_month(): return { "dateDescriptor" : "thisMonth" }
    def date_this_week(): return { "dateDescriptor" : "thisWeek" }
    def diamond_code( string ): return { "diamondCode" : str( string ) }
    def digital_id( int_ ): return { "digitalId" : str( int_ ) }
    def ean( string ): return { "ean" : str( string ) }
    def events( list_ ): return { "events" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def first_name( string ): return { "firstName": str( string ) }
    def first_name_starts_with( string ): return { "firstNameStartsWith" : str( string ) }
    def format_comic(): return { "format" : "comic" }
    def format_digest(): return { "format" : "digest" }
    def format_digital_comic(): return { "format" : "digital comic" }
    def format_graphic_novel(): return { "format" : "graphic novel" }
    def format_hardcover(): return { "format" : "hardcover" }
    def format_infinite_comic(): return { "format" : "infinite comic" }
    def format_magazine(): return { "format" : "magazine" }
    def format_trade_paperback(): return { "format" : "trade paperback" }
    def format_type_collection(): return { "formatType" : "collection" }
    def format_type_comic(): return { "formatType" : "comic" }
    def has_digital_issue( bool_ ): return { "hasDigitalIssue" : str( bool_ ).lower() }
    def isbn( string ): return { "isbn" : str( string ) }
    def issn( string ): return { "issn" : str( string ) }
    def last_name( string ): return { "lastName" : str( string ) }
    def last_name_starts_with( string ): return { "lastNameStartsWith" : str( stirng ) }
    def middle_name( string ): return { "middleName" : str( string ) }
    def middle_name_starts_with( string ): return { "middleNameStartsWith" : str( string ) }
    def modified_since( date ): return { "modifiedSince" : str( date ) }
    def name( string ): return { "name" : str( string ) }
    def name_starts_with( string ): return { "nameStartsWith" : str( string ) }
    def no_variants( bool_ ): return { "noVariants" : str( bool_ ).lower() }
    def order_by_FOC_date_ascending(): return { "orderBy" : "focDate" }
    def order_by_FOC_date_descending(): return { "orderBy" : "-focDate" }
    def order_by_first_name_ascending(): return { "orderBy" : "firstName" }
    def order_by_first_name_descending(): return { "orderBy" : "-firstName" }
    def order_by_id_ascending(): return { "orderBy" : "id" }
    def order_by_id_descending(): return { "orderBy" : "-id" }
    def order_by_issue_ascending(): return { "orderBy" : "issueNumber" }
    def order_by_issue_descending(): return { "orderBy" : "-issueNumber" }
    def order_by_last_name_ascending(): return { "orderBy" : "lastName" }
    def order_by_last_name_descending(): return { "orderBy" : "-lastName" }
    def order_by_middle_name_ascending(): return { "orderBy" : "middleName" }
    def order_by_middle_name_descending(): return { "orderBy" : "-middleName" }
    def order_by_modified_ascending(): return { "orderBy" : "modified" }
    def order_by_modified_descending(): return { "orderBy" : "-modified" }
    def order_by_name_ascending(): return { "orderBy" : "name" }
    def order_by_name_descending(): return { "orderBy" : "-name" }
    def order_by_sale_date_ascending(): return { "orderBy" : "onsaleDate" }
    def order_by_sale_date_descending(): return { "orderBy" : "-onsaleDate" }
    def order_by_start_date_ascending(): return { "orderBy" : "startDate" }
    def order_by_start_date_descending(): return { "orderBy" : "-startDate" }
    def order_by_start_year_ascending(): return { "orderBy" : "startYear" }
    def order_by_start_year_descending(): return { "orderBy" : "-startYear" }
    def order_by_suffix_ascending(): return { "orderBy" : "suffix" }
    def order_by_suffix_descending(): return { "orderBy" : "-suffix" }
    def order_by_tile_descending(): return { "orderBy" : "-title" }
    def order_by_title_ascending(): return { "orderBy" : "title" }
    def order_by_title_ascending(): return { "orderBy" : "title" }
    def order_by_title_descending(): return { "orderBy" : "-title" }
    def series( list_ ): return { "series" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def series_type_collection(): return { "seriesType" : "collection" }
    def series_type_limited(): return { "seriesType" : "limited" }
    def series_type_one_shot(): return { "seriesType" : "one shot" }
    def series_type_ongoing(): return { "seriesType" : "ongoing" }
    def start_year( int_ ): return { "startYear" : str( int_ ) }
    def stories( list_ ): return { "stories" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def suffix( string ): return { "suffix" : str( string ) }
    def teamups( list_ ): return { "sharedAppearances" : ",".join( list( map( lambda id_: str( id_ ), list_ ) ) ) }
    def title( string ): return { "title" : str( string ) }
    def title_starts_with( string ): return { "titleStartsWith" : str( string ) }
    def upc( string ): return { "upc" : str( string ) }

class ParameterError( Exception ): pass
