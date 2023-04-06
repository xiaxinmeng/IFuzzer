class C:
    def __init__ ( self, value ):
        self.value  =  value

    def __str__ ( self ):
        return "C<%s>" % self.value

    def __repr__ ( self ):
        return str(self)

    def __iadd__ ( self, x ):
        self.value  =  self.value + x