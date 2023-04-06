import io
class R(io.IOBase):
    def readline(self): return None

next(R())
