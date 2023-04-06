with open('file', 'ab') as f:
    f.write(b'abcd')
    f.seek(0)
    f.write(b'efgh')
    f.flush()

with open('file', 'rb') as f:
    print(f.read())