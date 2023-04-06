from io import BytesIO
import tokenize

# Round tripping fails on the second string.
table = (
r'''
print\
    ("abc")
''',
r'''
print \
    ("abc")
''',
)
for s in table:
    tokens = list(tokenize.tokenize(
        BytesIO(s.encode('utf-8')).readline))
    result = g.toUnicode(tokenize.untokenize(tokens))
    print(result==s)