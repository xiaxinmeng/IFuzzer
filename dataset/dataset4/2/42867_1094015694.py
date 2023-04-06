_buf = mmap.mmap(-1, 8192,
flags=mmap.MAP_PRIVATE|mmap.MAP_ANONYMOUS,
prot=mmap.PROT_READ|mmap.PROT_WRITE )