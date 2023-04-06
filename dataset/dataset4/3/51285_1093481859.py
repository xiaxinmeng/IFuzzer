class ac( object ):
    __slots__ = "a"

class bc( ac ):
    __slots__ = "b"

class cc( ac ):
    __slots__ = "c"

class cannotbecreated( bc,cc ):
     pass
     # raises an error.