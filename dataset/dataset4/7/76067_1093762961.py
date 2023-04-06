import multiprocessing
import multiprocessing.util
import logging

multiprocessing.util._logger = multiprocessing.util.log_to_stderr(logging.DEBUG)
import time
import ctypes


def crash_py_interpreter():
    print("attempting to crash the interpreter in ", multiprocessing.current_process())
    i = ctypes.c_char('a'.encode())
    j = ctypes.pointer(i)
    c = 0
    while True:
        j[c] = 'a'.encode()
        c += 1
    j


def test_fn(x):
    print("test_fn in ", multiprocessing.current_process().name, x)
    exit(0)

    time.sleep(0.1)


if __name__ == '__main__':

    # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=1)

    args_queue = [n for n in range(20)]

    # subprocess quits
    pool.map(test_fn, args_queue)