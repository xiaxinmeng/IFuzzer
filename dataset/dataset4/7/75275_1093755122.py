from multiprocessing import Process, Manager
from time import sleep
if __name__ == '__main__':
    with Manager() as manager:
        shared_list = manager.list()
        p = Process(target=sorted, args=(shared_list,))
        p.start()
        # sleep(0.5)
        shared_list = None
        p.join()