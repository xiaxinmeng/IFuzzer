script = """
print(a)
print([a for i in range(5)])
"""
exec(script, globals(), {"a":5})