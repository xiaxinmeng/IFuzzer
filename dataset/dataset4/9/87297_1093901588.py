fd = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
mapping = mmap.mmap(fd, 4096, flags=mmap.MAP_SHARED, prot=(mmap.PROT_READ | mmap.PROT_WRITE), offset=0x80000000)
mapping.write(bytearray([0x0,]* 4))  # results in 2 writes, should be 1
mapping.write(bytearray([0x0,]* 8))  # results in 4 writes, should be 1-2 depending on bus width (32b vs 64b)
# OR:
mapping[0:4] = struct.pack("=L", 0x0)  # results in 2 writes, should be 1