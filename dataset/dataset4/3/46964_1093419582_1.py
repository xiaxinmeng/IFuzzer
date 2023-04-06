args = eos_dl_args_t()
...
args_p = cast(pointer(args), c_void_ptr).value
fcntl.ioctl(fd, request, args_p)