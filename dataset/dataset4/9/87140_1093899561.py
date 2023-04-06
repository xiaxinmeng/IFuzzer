import io, tokenize

newline_token_1 = list(tokenize.tokenize(io.BytesIO("x\n".encode('utf-8')).readline))[-2]
newline_token_2 = list(tokenize.tokenize(io.BytesIO("x".encode('utf-8')).readline))[-2]

print(newline_token_1)
print(newline_token_2)