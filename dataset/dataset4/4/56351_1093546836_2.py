if _calcsize("l") == _calcsize("q"):
    # if long and long long have the same size, make c_longlong an alias for c_long
    c_longlong = c_long
    c_ulonglong = c_ulong
else:
    class c_longlong(_SimpleCData):
        _type_ = "q"
    _check_size(c_longlong)

    class c_ulonglong(_SimpleCData):
        _type_ = "Q"