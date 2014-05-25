class ImageAspectRatio:
    LANDSCAPE = { "landscape" : 1 }
    PORTRAIT = { "portrait" : 2 }
    STANDARD = { "standard" : 3 }

class ImageSize:
    SMALL = { "small" : 1 }
    MEDIUM = { "medium" : 2 }
    LARGE = { "large" : 3 }
    XLARGE = { "xlarge" : 4 }
    AMAZING = { "amazing" : 5 }
    FANTASTIC = { "fantastic" : 6 }
    INCREDIBLE = { "incredible" : 7 }
    UNCANNY = { "uncanny" : 8 }

class Image:
    def __init__( self, path, extension ): self.__path, self.__extension = path, extension
    def extension( self ): return self.__extension
    def detailed( self ): return "%s/%s.%s" % ( self.__path, "detail", self.__extension )
    def full( self ): return "%s.%s" % ( self.__path, self.__extension )
    def pixels( ratio, size ):
        return {
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.SMALL[ "small" ] ) : ( 120, 90 ),
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.MEDIUM[ "medium" ] ) : ( 175, 130 ),
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.LARGE[ "large" ] ) : ( 190, 140 ),
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.XLARGE[ "xlarge" ] ) : ( 270, 200 ),
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.AMAZING[ "amazing" ] ) : ( 250, 156 ),
            ( ImageAspectRatio.LANDSCAPE[ "landscape" ], ImageSize.INCREDIBLE[ "incredible" ] ) : ( 464, 261 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.SMALL[ "small" ] ) : ( 50, 75 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.MEDIUM[ "medium" ] ) : ( 100, 150 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.XLARGE[ "xlarge" ] ) : ( 150, 225 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.FANTASTIC[ "fantastic" ] ) : ( 168, 252 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.INCREDIBLE[ "incredible" ] ) : ( 216, 324 ),
            ( ImageAspectRatio.PORTRAIT[ "portrait" ], ImageSize.UNCANNY[ "uncanny" ] ) : ( 300, 450 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.SMALL[ "small" ] ) : ( 65, 45 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.MEDIUM[ "medium" ] ) : ( 100, 100 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.LARGE[ "large" ] ) : ( 140, 140 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.XLARGE[ "xlarge" ] ) : ( 200, 200 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.AMAZING[ "amazing" ] ) : ( 180, 180 ),
            ( ImageAspectRatio.STANDARD[ "standard" ], ImageSize.FANTASTIC[ "fantastic" ] ) : ( 250, 250 )
        } [ ( list( ratio.values() ) [ 0 ], list( size.values() ) [ 0 ] ) ]
    def ratios( size ):
        return {
            ImageSize.SMALL[ "small" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.PORTRAIT, ImageAspectRatio.STANDARD ],
            ImageSize.MEDIUM[ "medium" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.PORTRAIT, ImageAspectRatio.STANDARD ],
            ImageSize.LARGE[ "large" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.STANDARD ],
            ImageSize.XLARGE[ "xlarge" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.PORTRAIT, ImageAspectRatio.STANDARD ],
            ImageSize.AMAZING[ "amazing" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.STANDARD ],
            ImageSize.FANTASTIC[ "fantastic" ] : [ ImageAspectRatio.PORTRAIT, ImageAspectRatio.STANDARD ],
            ImageSize.INCREDIBLE[ "incredible" ] : [ ImageAspectRatio.LANDSCAPE, ImageAspectRatio.PORTRAIT ],
            ImageSize.UNCANNY[ "uncanny" ] : [ ImageAspectRatio.PORTRAIT ]
        } [ list( size.values() ) [ 0 ] ]
    def sizes( ratio ):
        return {
            ImageAspectRatio.PORTRAIT[ "portrait" ] : [ ImageSize.SMALL, ImageSize.MEDIUM, ImageSize.XLARGE, ImageSize.FANTASTIC, ImageSize.INCREDIBLE, ImageSize.UNCANNY ],
            ImageAspectRatio.STANDARD[ "standard" ] : [ ImageSize.SMALL, ImageSize.MEDIUM, ImageSize.LARGE, ImageSize.XLARGE, ImageSize.AMAZING, ImageSize.FANTASTIC ],
            ImageAspectRatio.LANDSCAPE[ "landscape" ] : [ ImageSize.SMALL, ImageSize.MEDIUM, ImageSize.LARGE, ImageSize.XLARGE, ImageSize.AMAZING, ImageSize.INCREDIBLE ],
        } [ list( ratio.values() ) [ 0 ] ]
    def thumbnail( self, ratio, size ): return "%s/%s_%s.%s" % ( self.__path, list( ratio.keys() ) [ 0 ], list( size.keys() ) [ 0 ], self.__extension )

