with io.BytesIO(b'abcd') as raw:
    with _pyio.TextIOWrapper(raw, encoding='ascii') as f:
        f.write("1")
        # read() must call writer.flush()
        assertEqual(f.read(1), 'b')
        # write() must rewind the raw stream
        f.write('2')
        assertEqual(f.read(), 'd')
        f.flush()
        assertEqual(raw.getvalue(), b'1b2d')

with io.BytesIO(b'abc') as raw:
    with _pyio.TextIOWrapper(raw, encoding='ascii') as f:
        self.assertEqual(f.read(1), b'a')
        # write() must undo reader readahead
        f.write(b"2")
        assertEqual(f.read(1), b'c')
        f.flush()
        assertEqual(raw.getvalue(), b'a2c')