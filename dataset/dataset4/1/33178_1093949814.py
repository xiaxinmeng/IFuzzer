class SpreadSheet:
    _cells = {}
    def __setitem__( self, key, formula ):
        self._cells[key] = formula
    def __getitem__( self, key ):
        return eval( self._cells[key], self )

ss = SpreadSheet()
ss['a1'] = '5'
ss['a2'] = 'a1*5'
ss['a2']