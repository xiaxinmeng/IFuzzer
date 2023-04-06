import multiprocessing as mp

def foo(q):
    q.put('hello')
    assert not q.empty()

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.SimpleQueue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()