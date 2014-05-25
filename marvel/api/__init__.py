class Api( object ):
    """ Base communication framework
    """
    def __init__( self ):
        from urllib.request import build_opener
        self.__opener = build_opener( _ApiErrorHandler() )
        import marvel.keys
        self.__keys = { "private" : marvel.keys.get( "private" ), "public" : marvel.keys.get( "public" ) }
        self._attribute = { }
        for element in Api.attributes(): self._attribute[ element ] = None
    def attributes( self = None ): return [ "attributionText", "code", "copyright", "data", "etag", "status" ]
    def attribution( self ): return self._attribute[ "attributionText" ]
    def call( self, endpoint, data = "", etag = None ):
        headers = { "Accept-Encoding" : "gzip" }  if etag is None else { "Accept-Encoding" : "gzip", "If-None-Match" : etag }
        import marvel.auth
        from urllib.request import Request
        # data must be omitted, because Marvel API currently doesn't accept POST
        request = Request( "%s?%s%s%s" % ( endpoint, marvel.auth.get( self.__keys ), "" if data is "" else "&", data ), headers = headers )
        from urllib.error import HTTPError
        try:
            with self.__opener.open( request ) as resource:
                from gzip import decompress
                from json import loads
                response = loads( decompress( resource.read() ).decode() )
        except HTTPError: return self # errors will be caught by ApiErrorHandler
        for key in list( filter( lambda key: key not in [ "data" ], Api.attributes() ) ): self._attribute[ key ] = response[ key ]
        from marvel.api.data import Data
        self._attribute[ "data" ] = Data( response[ "data" ] )
        return self
    def code( self ): return self._attribute[ "code" ]
    def copyrigth( self ): return self._attribute[ "copyright" ]
    def data( self ): return self._attribute[ "data" ]
    def endpoint( self = None ): return "http://gateway.marvel.com/v1/public/"
    def etag( self ): return self._attribute[ "etag" ]
    def status( self ): return self._attribute[ "status" ]

class ApiError( Exception ):
    def __init__( self, message ):
        from gzip import decompress
        from json import loads
        response = loads( decompress( message.read() ).decode() )
        # TODO: properly
        print("Error %d (%s: %s)" % ( message.status, response[ "code" ], response[ "message" ] ) )

from urllib.request import BaseHandler
class _ApiErrorHandler( BaseHandler ):
    def http_error_304( self, req, fp, code, msg, hdrs ): pass
    def http_error_401( self, req, fp, code, msg, hdrs ): raise ApiError( fp )
    def http_error_403( self, req, fp, code, msg, hdrs ): raise ApiError( fp )
    def http_error_404( self, req, fp, code, msg, hdrs ): raise ApiError( fp )
    def http_error_405( self, req, fp, code, msg, hdrs ): raise ApiError( fp )
    def http_error_409( self, req, fp, code, msg, hdrs ): raise ApiError( fp )

