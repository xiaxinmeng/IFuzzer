def the_factory( parm1 ):
    class the_class( object ):
        def curried( self ): return parm1
    return the_class

x = the_factory( 42 )

y = x( )