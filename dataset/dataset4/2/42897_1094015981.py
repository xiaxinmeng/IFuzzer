import threading

class foo:
    def __getattr__(self, x): self.foo

def j(): foo().bar

t = threading.Thread(target=j, args=())
t.start()