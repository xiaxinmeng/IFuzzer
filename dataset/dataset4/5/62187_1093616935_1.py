with captured_stdin() as s:
    s.write('hello\n')
    s.seek(0)
    captured = input()