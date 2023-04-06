import io

raw = io.BytesIO(bytes(200))
buffered = io.BufferedReader(raw, 10)

data = buffered.read(20)
print('Read %d bytes using read()' % len(data))

data = buffered.read1(20)
print('Read %d bytes using read1()' % len(data))