import fileinput

fi = fileinput.input('test_fileinput.py', mode='rb')

while True:
    line = fi.readline()
    assert isinstance(line, bytes)
    if not len(line):
        break