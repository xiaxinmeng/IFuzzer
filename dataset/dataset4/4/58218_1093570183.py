i = filter(bool, range(5))
for _ in range(1000000):
    i = filter(bool, i)

for p in i:
    print(p)