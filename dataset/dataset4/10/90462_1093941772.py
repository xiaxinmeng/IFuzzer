def read_lines(path):
    with path.open() as strm:
        yield from strm