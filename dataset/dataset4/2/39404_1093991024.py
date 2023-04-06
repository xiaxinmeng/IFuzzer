_mathEnv = {'__builtins__': new.module('__builtins__'), 'i': 1j}
_mathEnv.update(math.__dict__)
_mathEnv.update(cmath.__dict__)