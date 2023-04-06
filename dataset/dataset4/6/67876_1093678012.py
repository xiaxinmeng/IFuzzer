if not isinstance(data, bytes):
    data = memoryview(data).cast('B')