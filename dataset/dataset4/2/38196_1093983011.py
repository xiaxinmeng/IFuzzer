def getint( s ):
    try:
        return int( s )
    except ValueError:
        return s