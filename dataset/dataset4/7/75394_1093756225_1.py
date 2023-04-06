# snippet pip code
def _is_running_32bit():
    return sys.maxsize == 2147483647
    
if result == "linux_x86_64" and _is_running_32bit():
    # 32 bit Python program (running on a 64 bit Linux): pip should only
    # install and run 32 bit compiled extensions in that case.
    result = "linux_i686"