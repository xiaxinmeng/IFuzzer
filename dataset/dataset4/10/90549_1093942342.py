
import multiprocessing as mp

global_resource = mp.Semaphore()

def submain(): pass

if __name__ == '__main__':
    p = mp.Process(target=submain)
    p.start()
    p.join()
