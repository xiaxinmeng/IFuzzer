import sys, time, multiprocessing
from multiprocessing.pool import ThreadPool

def main():
    # Launch 8 workers
    pool = ThreadPool(8)
    it = pool.imap(run, range(500))
    while True:
        try:
            it.next()
        except StopIteration:
            break

def run(value):
    # Each worker launch its own Process
    process = multiprocessing.Process(target=run_and_might_segfault,     args=(value,))
    process.start()

    while process.is_alive():
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.1)

    # Will never join after a while, because of a mystery deadlock
    process.join()

def run_and_might_segfault(value):
    print(value)

if __name__ == '__main__':
    main()