
_tran = defaultdict(lambda: 'x')
 # _tran = {}
_tran.update((ord(c), ord('(')) for c in "({[")
_tran.update((ord(c), ord(')')) for c in ")}]")
_tran.update((ord(c), ord(c)) for c in "\"'\\\n#")
# _tran = StringTranslatePseudoMapping(_tran, default_value=ord('x'))
