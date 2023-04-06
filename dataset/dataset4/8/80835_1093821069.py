# tokenize_example.py
import tokenize
f = open('example.py', 'rb')
token_gen = tokenize.tokenize(f.readline)

for token in token_gen:
    # Something like this
    # TokenInfo(type=1 (NAME), string='class', start=(1, 0), end=(1, 5), line='class Foo:\n')
    # TokenInfo(type=1 (NAME), string='Foo', start=(1, 6), end=(1, 9), line='class Foo:\n')
    # TokenInfo(type=53 (OP), string=':', start=(1, 9), end=(1, 10), line='class Foo:\n')
    print(token)