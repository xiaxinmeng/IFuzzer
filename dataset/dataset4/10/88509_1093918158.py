a = ContextVar('a')
token = a.set(1234)
...
a.reset(token)