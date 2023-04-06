a = ['abc\n']
b = ['abcd\n', 'def\n']
for line in difflib.Differ().compare(a,b): print(line, end='')