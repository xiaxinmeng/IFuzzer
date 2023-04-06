import os
import resource
import random

print("1")

for fd in range(resource.getrlimit(resource.RLIMIT_NOFILE)[0]):
    try:
        if fd not in range(0, 3):
            os.close(fd)
    except os.error:
        pass

print("2")
print(os.urandom(32))
print("3")