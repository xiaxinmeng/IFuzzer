def foo(s): return len(s)
code = foo.__code__
FunctionType = type(foo)
f = FunctionType(code, {"__builtins__": {"len": len}})
print(f("abc"))
f.__builtins__.clear()
print(f("abc"))