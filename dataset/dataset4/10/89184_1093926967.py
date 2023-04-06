from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep

def submit(pool):
    pool.submit(submit, pool)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(1)
    pool.submit(submit, pool)

    while True:
        with ProcessPoolExecutor() as workers:
            print('WORK')
            workers.submit(sleep, 0.01).result()
            print('DONE')
        print('OK')