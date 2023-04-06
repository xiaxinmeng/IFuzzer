def f():
    class A:
        def __lt__(self, other):
            nonlocal x
            x += 100
            return True
    a = A()
    x = 1
    print(a < x < 10)
    x = 1
    print(a < x and x < 10)