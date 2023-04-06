if LONG_MAX == PY_SSIZE_T_MAX == (1 << 31) - 1:
    class MyArray(Array):
        _type_ = c_longlong
        _length_ = 1 << 29

    arr = MyArray()
    for i in range(3):
        arr[i] = i
    for i in range(3):
        print(arr[i])