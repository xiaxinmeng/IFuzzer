def test_iter():
    # getting iterator from a temporary file should keep it alive
    # as long as it's being iterated over
    lines = [b'spam\n', b'eggs\n', b'beans\n']
    def make_file():
        f = tempfile.NamedTemporaryFile(mode='w+b')
        f.write(b''.join(lines))
        f.seek(0)
        return iter(f)
    for i, l in enumerate(make_file()):
        print(l, lines[i])

test_iter()