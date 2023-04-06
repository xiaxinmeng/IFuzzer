EOS_IOC_MAGIC = 0xF4
request = IOC(IOC_WRITE, EOS_IOC_MAGIC, 0x00, 0) # ignore size

err = ioctl (fd, request, args)