string_io = io.StringIO(text)
tokens = list(
    tokenize.generate_tokens(string_io.readline)
)