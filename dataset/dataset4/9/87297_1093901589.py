import os, mmap
fd = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
mapping = mmap.mmap(fd, 4096, flags=mmap.MAP_SHARED, prot=(mmap.PROT_READ | mmap.PROT_WRITE), offset=0x80000000)
mv = memoryview(mapping)
mv_as_int32 = mv.cast('I')  # Note "I" works as intended, "L" still results in duplicate writes; "LL" is not an option
mv_as_int32[0x0 // 4] = 0xDEADBEEF  # this works; results in 1 write issued on the AXI bus