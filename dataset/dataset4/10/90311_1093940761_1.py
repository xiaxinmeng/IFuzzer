code = """
def outer():
    a = 1
    def f():
        return a
    return f

f = outer()
print(f())
"""
exec(code, {}, {})