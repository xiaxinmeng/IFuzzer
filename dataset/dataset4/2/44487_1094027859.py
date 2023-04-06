class TrivialContext:
    def __enter__(self): return self
    def __exit__(self,*exc_info): pass

def f():
    with TrivialContext() as tc:
        return 1
f()