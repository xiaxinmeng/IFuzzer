import concurrent.futures
import time

def worker():
    return time.perf_counter()

if __name__ == '__main__':
    pool = concurrent.futures.ProcessPoolExecutor()
    futures = []
    for i in range(3):
        print('Submitting worker {:d} at time.perf_counter() == {:.3f}'.format(i, time.perf_counter()))
        futures.append(pool.submit(worker))
        time.sleep(1)

    for i, f in enumerate(futures):
        print('Worker {:d} started at time.perf_counter() == {:.3f}'.format(i, f.result()))