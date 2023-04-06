
import os, subprocess

def show_fds():
    for entry in os.scandir("/proc/self/fd"):
        print(entry.name, "->", os.readlink(entry.path))

print("Before:")
show_fds()

# Trigger an error when trying to open /dev/null
os.devnull = "/NOEXIST"

try:
    subprocess.Popen(["ls"], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)
except FileNotFoundError as e:  # "User must be a string or an integer"
    print(e)

print("After:")
show_fds()
