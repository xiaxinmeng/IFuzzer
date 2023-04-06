import multiprocessing as mp
from queue import Empty
import os
import sys
import time


def process_worker(input_q: mp.Queue):
    print(f'process_worker, pid={os.getpid()}, executable={sys.executable}')
    while True:
        try:
            inp = input_q.get_nowait()
            if inp == 'STOP':
                break
            execute_job(inp)
        except Empty:
            pass


def execute_job(input_args):
    print(f'Executing job {input_args}')


def main_process_experiment():
    print(f"main, pid={os.getpid()}, executable={sys.executable}")
    input_q = mp.Queue()

    p = mp.Process(target=process_worker, args=(input_q, ))
    p.start()
    time.sleep(0.5)

    print('submitting...')
    for i in range(3):
        print(f'submitting {i}')
        input_q.put(i)
    input_q.put('STOP')

    p.join()


if __name__ == '__main__':
    main_process_experiment()