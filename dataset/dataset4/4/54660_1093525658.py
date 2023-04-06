import io, mmap
io.BytesIO(b' ').readinto(memoryview(mmap.mmap(-1, 1, prot=mmap.PROT_READ)))