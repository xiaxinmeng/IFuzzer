def hi(threadlocal=threading.local()):
    ...

class Hi:
    threadlocal = threading.local()
    def __call__(self):
        ...  # change threadlocal to self.threadlocal

hi = Hi()