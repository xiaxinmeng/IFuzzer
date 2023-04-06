class A:
    def __del__(self):
        self.recurse(47)
    def recurse(self, n):
        if n:
            self.recurse(n-1)
        else:
            raise ValueError