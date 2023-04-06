def foo():
    local_to_launch = subprocess.Popen("/bin/echo")
    return local_to_launch

local_to_launch = foo()