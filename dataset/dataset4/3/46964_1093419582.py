args = struct.pack("iP", len(c), cast (pointer (c), c_void_p).value)
fcntl.ioctl(fd, request, args)