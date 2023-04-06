import inspect
s = inspect.signature(lambda **kwargs: kwargs).bind()
s.arguments["foo"] = 12