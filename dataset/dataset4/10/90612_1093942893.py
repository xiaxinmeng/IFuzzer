import os

print(os.get_inheritable(0))

fd_null_before_close = os.open("/dev/null", os.O_RDWR)
os.close(0)
fd_null = os.open("/dev/null", os.O_RDWR)

print(fd_null_before_close)
print(fd_null)

os.dup2(fd_null, 0)
print(os.get_inheritable(0))

os.dup2(fd_null_before_close, 0)
print(os.get_inheritable(0))