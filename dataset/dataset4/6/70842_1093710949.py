import pathlib
p = pathlib.Path('.')
print(list(p.glob('*.txt')))
print(list(p.glob('Mixedcase.txt')))