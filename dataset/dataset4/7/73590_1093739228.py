if PY2:
    def helper(arg):
        if isinstance(ar, (int, long)):
            return chr(arg)
        return arg
else:
    def helper(arg):
        return arg
...
v[0] = helper(42)