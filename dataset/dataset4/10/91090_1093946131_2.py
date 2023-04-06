
import multiprocessing

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')  # or 'forkserver' but not 'fork'
    process_a = multiprocessing.Process()
    process_b = multiprocessing.Process()
    process_b.foo = process_a
    process_a.start()  # creates process_a._popen.finalizer._weakref
    process_b.start()  # TypeError: cannot pickle 'weakref' object
