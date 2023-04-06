class C:
    def __del__(self):
        print("Calling C destructor.")

def foo():
    c = C()
    import pdb; pdb.set_trace()
    c = 1

foo()