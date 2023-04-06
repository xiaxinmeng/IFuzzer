import threading
import sys

if sys.version_info.major == 3:
    xrange = range

def main():
    size = 1024 * 1024 # large enough
    f = open("__temp__.tmp", "w", size)
    for _ in xrange(size):
        f.write("c")
    t1 = threading.Thread(target=f.close)
    t2 = threading.Thread(target=f.close)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()