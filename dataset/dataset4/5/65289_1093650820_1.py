import io, os
read, write = os.openpty()
os.write(write, b'ok\n')
os.close(write)
with io.FileIO(read, closefd=False) as fp:
    print(fp.readall())