
class Wrapper:
        @staticmethod
        def __getattr__(item):
                return repr(item) # dummy

a = Wrapper()
print(a.foo)
