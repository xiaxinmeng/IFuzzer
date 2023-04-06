with io.BytesIO(b'abcd') as raw:
    with _pyio.TextIOWrapper(raw, encoding='ascii') as f:
        f.read(1)
        f.write('2')
        f.tell()