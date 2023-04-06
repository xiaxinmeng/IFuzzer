def f(x, y):
    class A:
        def __init__(self, value):
            self.value = value
        def __del__(self):
            print(a, b)
        def __repr__(self):
            return f"<value={self.value}>"

    a = A(333)
    b = A(444)
    a, b = x, y

f(1, 2)