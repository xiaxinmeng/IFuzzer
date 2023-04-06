def f():
    script = """
print(a)
print([a for i in range(5)])
    """
    a = 5
    exec(script)
    
f()