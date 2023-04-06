class A(object):
    def method(self):
        print("from class A")

class B(A):
    def method(self):
        print("bad method")
        # This is bad, don't do it!
        super(type(self), self).method()

class C(B): pass