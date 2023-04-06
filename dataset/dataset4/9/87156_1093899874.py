def foo(): return len("abc")
code = foo.__code__
g = {"__builtins__": {"len": len}}
f = FunctionType(code, g)
f()  # Succeeds
g["__builtins__"] = {}
f()  # Fails in 3.9 and before, passes in 3.10