def f(): pass

import marshal
badstring=marshal.dumps(f.func_code).replace('(\x01\x00\x00\x00N',
'(\x00\x00\x00\x00')