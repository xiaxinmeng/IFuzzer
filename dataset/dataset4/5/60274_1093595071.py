from ctypes import *

class cbs( BigEndianStructure ):
    __slots__ = tuple()
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self.a = 11

class cls( LittleEndianStructure ):
    __slots__ = tuple()
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self.a = 11

class cs( Structure ):
    __slots__ = tuple()
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self.a = 11