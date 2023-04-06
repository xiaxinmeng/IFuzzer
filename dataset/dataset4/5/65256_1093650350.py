from io import TextIOWrapper, BytesIO
class MyByteStream(BytesIO):
    def read1(self, len_):
        return memoryview(super().read(len_))
bs = MyByteStream(b'some data in ascii\n')
ss = TextIOWrapper(bs, encoding='ascii')
print(ss.read(200))