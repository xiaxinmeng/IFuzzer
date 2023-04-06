parser = HTMLParser()
for chunk in pipe_in_html():
    yield from parser.tokenize(chunk)