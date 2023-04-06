class groupby:
    def __init__( self , iterable , key_function = ( lambda x: x ) ):
        self.iterable = iter( iterable )
        self.key_function = key_function
        self.FINISHED = object()
        try:
            self.next_value = next( self.iterable )
        except StopIteration: 
            self.next_value = self.FINISHED
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.next_value == self.FINISHED:
            raise StopIteration
        self.group_key_value = self.key_function( self.next_value )
        return ( self.group_key_value , self._group() )
    def _group( self ):
        while self.next_value != self.FINISHED \
          and self.group_key_value == self.key_function( self.next_value ):
            yield self.next_value
            try:
                self.next_value = next( self.iterable )
            except StopIteration:
                self.next_value = self.FINISHED 
        return