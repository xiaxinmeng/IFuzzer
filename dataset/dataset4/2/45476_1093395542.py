if not args:
    return self._getdoubles(self.tk.call(self._w, 'xview'))
self.tk.call((self._w, 'xview') + args)