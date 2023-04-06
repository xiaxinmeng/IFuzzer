import multiprocessing as mp

def subProcFn(m1):
    pass
    
if __name__ == "__main__":

    __spec__ = None
    
    m1 = mp.Manager()
    
    p1 = mp.Process(target=subProcFn, args=(m1,))
    p1.start()
    p1.join()