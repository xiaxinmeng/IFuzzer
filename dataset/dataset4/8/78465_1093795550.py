result = type.__new__(type, *args)
if isinstance(result, type):
    result.__init__(*args)