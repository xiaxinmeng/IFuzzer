class eos_dl_args_t (Structure):
    _fields_ = [("length", c_ulong),
                ("data", c_void_p)]