class Summary( object ):
    """ A summary basically is a link to resource, which can be called by user.
        Base class used by API entities.
    """
    def __init__( self, dict_, type_ ):
        self.__attribute = { }
        self.__attribute[ "resourceURI" ], self.__attribute[ "name" ], self.__type = dict_[ "resourceURI" ], dict_[ "name" ], type_
    def attributes( self = None ): return [ "resourceURI", "name" ]
    def call( self ): return self.__type( self.__attribute[ "resourceURI" ].rsplit( "/", 1 ) [ 1 ] ).call() # we only need id, has all the info for single entry
    def name( self ): return self.__attribute[ "name" ]
    def resource( self ): return self.__attribute[ "resourceURI" ]

class SummaryCollection( object ):
    """ Container class for a list of summaries.
        Fields are metadata about the list.
        Base class used by API entities.
    """
    def __init__( self, dict_, type_ ):
        self.__attribute = { }
        self.__attribute[ "total" ], self.__attribute[ "resourceURI" ], self.__attribute[ "items" ], self.__attribute[ "count" ], self.__type = dict_[ "available" ], dict_[ "collectionURI" ], list( map( lambda dict_: Summary( dict_, type_ ), dict_[ "items" ] ) ), dict_[ "returned" ], type_
    def attributes( self = None ): return [ "total", "resourceURI", "items", "count" ]
    def call( self ): return self.__type.collection()( self.__attribute[ "resourceURI" ] ).call()
    def count( self ): return self.__attribute[ "count" ]
    def items( self ): return self.__attribute[ "items" ]
    def resource( self ): return self.__attribute[ "resourceURI" ]
    def total( self ): return self.__attribute[ "total" ]

