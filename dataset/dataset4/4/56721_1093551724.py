import codecs
_open = codecs.open
#_open = open
filename = "test"
with _open(filename, 'w', encoding='utf_16') as f:
    f.write('abc')
with _open(filename, 'a', encoding='utf_16') as f:
    f.write('def')
with _open(filename, 'r', encoding='utf_16') as f:
    content = f.read()
    assert content == 'abcdef', ascii(content)