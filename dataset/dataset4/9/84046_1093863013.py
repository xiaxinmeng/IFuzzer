class A:
    @property
    def myprop(self):
        print("property called")
        a = 1
        a.foo  # <-- AttributeError that should not be silenced

    def __getattr__(self, attr_name):
        print("__getattr__ called")

a = A()
a.myprop