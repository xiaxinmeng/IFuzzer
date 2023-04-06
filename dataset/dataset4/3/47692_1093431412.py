def readline(self, *args, **kwargs):
    v = self.input.readline(*args, **kwargs)
    assert_(type(v) is type(""))
    return v