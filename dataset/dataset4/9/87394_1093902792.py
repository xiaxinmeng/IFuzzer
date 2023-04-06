def func(s):
    return len(s)

text = "abc"
print(func(text))

FuncType = type(func)
func_globals = {"__builtins__":__builtins__.__dict__}
code = func.__code__
func2 = FuncType(code, func_globals)

print(func2(text))