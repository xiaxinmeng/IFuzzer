def func(s): return len(s)

code = func.__code__
FuncType = type(func)

func2_globals = {}
func2 = FuncType(code, func2_globals)
# func2.func_builtins = {'None': None}
func2.__globals__['__builtins__'] = __builtins__

# frame created with {'None': None} builtins: "len" key is missing
func2("abc")