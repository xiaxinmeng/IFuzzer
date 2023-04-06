def handler(signum, frame):
        import traceback
        print(''.join(traceback.format_stack(frame)))

signal.signal(signal.SIGTERM, handler)

p1 = ThreadPool()

class Foo(object):
    def a(self):
        print("a")
        return 1

    def do(self):
        return p1.apply_async(self.a)


foo = Foo()
r = foo.do()

print(r.get())
p1.close()
p1.join()