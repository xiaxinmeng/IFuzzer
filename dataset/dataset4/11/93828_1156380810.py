from ast import parse, dump

node = parse('from temp import A, B\n\nA.y = 10\n\nB.y = 5\n\n\n')
print(dump(node))