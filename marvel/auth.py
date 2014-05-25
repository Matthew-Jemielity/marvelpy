class Timestamp( object ):
    def __init__( self, magnitude ): self.__magnitude = magnitude
    def __call__( self, function ):
        from random import randint
        from time import time
        return lambda *args, **kwargs: function( str( int( time() ) * self.__magnitude + randint( 0, self.__magnitude ) ), *args, **kwargs )

def get( dictionary ):
    try:
        if ( dictionary[ "private" ] is not str( dictionary[ "private" ] ) ) or ( dictionary[ "public" ] is not str( dictionary[ "public" ] ) ): return None
    except ( TypeError, KeyError ): return None
    @Timestamp( 1000000 )
    def encode( timestamp, private, public ):
        from hashlib import md5
        from urllib.parse import urlencode
        return urlencode( { "ts" : timestamp, "apikey" : public, "hash" : md5( ( timestamp + private + public ).encode() ).hexdigest() } )
    return encode( dictionary[ "private" ], dictionary[ "public" ] )

