if isinstance(stdin, io.BytesIO):
    inputdata = stdin.read()
    stdin = PIPE