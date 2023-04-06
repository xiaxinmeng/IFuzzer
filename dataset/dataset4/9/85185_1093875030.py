import os

fd = os.memfd_create("Hi", os.MFD_CLOEXEC)
if fd == -1:
    print("boo")
    os.exit(1)

if os.get_inheritable(fd):
    print("inheritable, boo")
    os.exit(1)

with open(fd, "wb", closefd=False) as f:
    f.write(b'memfd_create')
    if f.tell() != 12:
        print("Hork")
        os.exit(1)
    print("What?")

print("Done")