def yielder (fileobj):
    yield from fileobj

with open('some_test_file', 'w') as f:
    f.write('line one\nline two\nline three')

with open('some_test_file', 'r') as f:
    line = next(yielder(f))
    nline = next(f)