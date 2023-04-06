import _pyio, io

with io.BytesIO(b'abc') as raw:
    #with _pyio.BufferedRandom(raw) as f:
    with io.BufferedRandom(raw) as f:
        f.write(b"X")
        print("pos?", f.tell(), raw.tell())
        print(f.read())