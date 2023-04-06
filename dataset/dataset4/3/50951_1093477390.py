def xview(self,*args):
    """Query and change horizontal position of the view."""
    #modify
    if not args:
        return self._getdoubles(self.tk.call(self._w, 'xview'))
    #old code
    index=args[0]
    self.tk.call(self._w, 'xview', index)