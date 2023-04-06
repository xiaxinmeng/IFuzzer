def clipper(max):
    for i in range(5):
        if i < max:
            yield i

class Foo:
    x = 3
    y = list(clipper(x))

print(Foo.y)
# [0, 1, 2]