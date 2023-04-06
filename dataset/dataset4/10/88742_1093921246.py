class A:
    def b(self):
        1 / 0


x = (
    A()
        .b()
)