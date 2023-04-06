
def hack_c():
    c = C()
    def _(*args, **kwargs):
        return c(*args, **kwargs)
    return _
A.__del__ = hack_c()
