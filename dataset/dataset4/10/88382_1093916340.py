class MyClass:
    def do_something(self, a, b = []):
        b.append(a)
        print("b contains", b)
    def caller(self):
        a = (1,2)
        self.do_something(a)

a = MyClass().caller()
a = MyClass().caller()
a = MyClass().caller()