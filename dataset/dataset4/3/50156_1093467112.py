import multiprocessing as mp
from time import sleep

def e(tag):
    for i in range(10):
        print(tag, i)
        sleep(1)

if __name__ == '__main__':
    p = mp.Process(target=e, args=("daemon",), daemon=True)
    q = mp.Process(target=e, args=("normal",))
    p.start()
    q.start()
    sleep(5)