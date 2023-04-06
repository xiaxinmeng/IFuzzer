import io
with io.TextIOWrapper(io.BytesIO(b'.\r\n...\r\n\r\n\r\n')) as fp:
    fp.readline() # '.\n'
    fp.readline() # '......\n'
    print(fp.tell()) # 18446744073709551628 = 0x10000000000000009