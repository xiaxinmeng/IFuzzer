import operator

N = 500000
l = [0]

for i in range(N):
    l = map(operator.add, l, [1])

print(list(l))
