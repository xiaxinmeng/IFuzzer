
import io

def take(stream):
    return stream.read(1)

def tokenize(stream):
    take(stream)
    take(stream)
    take(stream)
    print('-----> tell:', stream.tell())

with io.BytesIO(b'"")\r\nx\r\n') as f:
    tokenize(io.TextIOWrapper(f))
