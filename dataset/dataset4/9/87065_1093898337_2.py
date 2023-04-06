
class A:
    def __bool__(self):
        print("BOOL")
        return False

a = A()
if a:
   pass
