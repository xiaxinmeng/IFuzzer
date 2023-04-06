args = eos_dl_args_t()
args.length = len (c)
args.data = cast (pointer (c), c_void_p)

from eioctl import *