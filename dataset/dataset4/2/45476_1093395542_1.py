res = self.tk.call(self._w, 'xview', *args)
if args:
    return self._getdoubles(res)