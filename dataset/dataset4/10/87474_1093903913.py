
import os, subprocess

def show_fds():
    for entry in os.scandir("/proc/self/fd"):
        print(entry.name, "->", os.readlink(entry.path))

print("Before:")
show_fds()

try:
    subprocess.Popen(["ls"], stdin=subprocess.PIPE, user=1.0)
except TypeError as e:  # "User must be a string or an integer"
    print(e)

print("After:")
show_fds()
