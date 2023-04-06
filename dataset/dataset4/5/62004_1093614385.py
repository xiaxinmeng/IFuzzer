def grouper(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i: i + size]

unpack = struct.Struct('!I').unpack
for chunk in grouper(data, 4):
    word, = unpack(chunk)
    ...