d = {'metaclass': type}
for _ in [1]:
    class A(1, 2, 3, **d):
        pass