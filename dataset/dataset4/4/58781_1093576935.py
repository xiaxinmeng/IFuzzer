import io
class DummyOut(io.IOBase):
    def write(self, s):
        return len(s)

dum = DummyOut()
print(dum.write('sixsix'))
# 6