def foo(data):
    data = memoryview(data)
    if data:
        data = data.cast('B')
    else:
        data = b''