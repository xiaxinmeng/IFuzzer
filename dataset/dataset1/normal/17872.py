import io, marshal

class BadReader(io.BytesIO):
    def read(self, n=-1):
        b = super().read(n)
        print('read', n, b)
        if n is not None and n > 4:
            b += b' ' * 10**6
        return b

d = marshal.dumps('abcdefgh')
print(marshal.load(BadReader(d)))
