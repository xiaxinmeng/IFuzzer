class Foo:
    x = 3
    y = []
    for z in range(5):
        if z < x:
            y.append(z)

print(Foo.y)
# [0, 1, 2]