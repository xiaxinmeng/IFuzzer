a = [0, 1, 2, 3, 4, 1, 2, 3, 5]

for i in a:
    if a.count(i) > 1:
        a.remove(i)

print(a)