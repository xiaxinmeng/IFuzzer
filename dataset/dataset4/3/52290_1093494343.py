import io,mmap

b = io.BytesIO("abc")
m = mmap.mmap(-1,10)
m.seek(5)
b.readinto(m)