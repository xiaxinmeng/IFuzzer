
import torch.multiprocessing as mp

mp.current_process().authkey = b'abc'

def start_client(manager, host, port, key):
    manager.register('get_list')
    manager.__init__(address=(host, port), authkey=key)
    manager.connect()
    return manager

def logic(manager):
    l = manager.get_list()
    for i in range(len(l)):
        if not l[i].is_set():
            l[i].set()
            print('set')

if __name__=='__main__':
    manager = mp.Manager()
    manager = start_client(manager, '127.0.0.1', 5000, b'abc')
    logic(manager)
