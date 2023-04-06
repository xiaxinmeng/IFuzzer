def test_readline():
    for mode in ('r', 'rb', 'r+', 'r+b'):
        f = open(__file__, mode)
        try:
            f.readline(0.1)
        except TypeError:
            tmp = f.readline()
        f.close()
    print('OK')

test_readline()