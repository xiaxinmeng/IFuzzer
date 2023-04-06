import os

def main():
    r, w = os.pipe()
    f_w = os.fdopen(w, "w")
    f_w.buffer.write(b"a" * 65536)
    f_w.buffer.write(b"b")

main()