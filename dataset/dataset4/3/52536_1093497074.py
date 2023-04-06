from multiprocessing import Process

class Unpicklable(object):
    def __reduce__(self):
        raise RuntimeError

class MyProcess(Process):
    def __init__(self, foo, unpicklable_bar):
        Process.__init__(self,
                         #args=(foo, unpicklable_bar)
                         )
        self.foo = foo
        self.baz = str(unpicklable_bar)

    def run(self):
        print(self.foo)
        print(self.baz)

if __name__ == '__main__':
    p = MyProcess([1,2,3], Unpicklable())
    p.start()
    p.join()