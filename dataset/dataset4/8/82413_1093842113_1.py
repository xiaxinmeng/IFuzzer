lp = self.username
if not parser.DOT_ATOM_ENDS.isdisjoint(lp):
    lp = parser.quote_string(lp)