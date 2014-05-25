def get( which ):
    try:
        with open( "marvel/keys/%s" % which, "r" ) as key: return key.read()
    except ( OSError, IOError ): return None

