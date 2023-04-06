tokens = list(tokenize.tokenize(io.BytesIO(source.encode('utf-8')).readline))
ellipsis = tokens[1]

print(ellipsis)
print(token.ELLIPSIS) 