from _pyio import open

with open('test.txt', 'w', encoding='utf-8-sig') as fp:
    print("abc", file=fp)
    print("d\xe9f", file=fp)

with open('test.txt', 'r') as fp:
    print("open().read(): {!r}".format(fp.read()))