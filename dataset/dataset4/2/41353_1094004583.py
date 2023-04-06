def siginterrupt(signum, flag):
    """change restart behavior when a function is interrupted by the 
    specified signal. see man siginterrupt.
    """
    import ctypes
    import sys
    
    if flag:
        flag = 1
    else:
        flag = 0
        
    if sys.platform=='darwin':
        libc = ctypes.CDLL("libc.dylib")
    elif sys.platform=='linux2':
        libc = ctypes.CDLL("libc.so.6")
    else:
        libc = ctypes.CDLL("libc.so")

    if libc.siginterrupt(signum, flag)!=0:
        raise OSError("siginterrupt failed")