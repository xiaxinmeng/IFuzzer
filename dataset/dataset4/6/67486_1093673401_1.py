import tokenize

with tokenize.open('hello.py') as f:
    token_gen = tokenize.tokenize(f.readline)
    for token in token_gen:
        print(token)