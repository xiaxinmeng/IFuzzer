
import os, psutil
import numpy as np
from multiprocessing import Process, shared_memory

SHM_SIZE = 100000 * 30 * 20


def f(name):
    print('[Sub] (Before) Used Memory of {}: {} MiB'.format(
        os.getpid(),
        psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
        ))
    shm = shared_memory.SharedMemory(name=name)
    b = np.ndarray(shape=(SHM_SIZE, 1), dtype=np.float64, buffer=shm.buf)
    for i in range(SHM_SIZE):
        b[i, 0] = 1
    print('[Sub] (After) Used Memory of {}: {} MiB'.format(
        os.getpid(),
        psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
        ))


def main():
    print('[Main] Used Memory of {}: {} MiB'.format(
        os.getpid(),
        psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
        ))
    shm = shared_memory.SharedMemory(create=True, size=8*SHM_SIZE, name='shm')
    p = Process(target=f, args=('shm',))
    p.start()
    p.join()
    print('[Main] Used Memory of {}: {} MiB'.format(
        os.getpid(),
        psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
        ))
    input()
    shm.close()
    shm.unlink()


if __name__ == '__main__':
    main()
