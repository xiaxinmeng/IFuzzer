import multiprocessing as mp

def f(d):
  d['f'] = {}
  d['f']['msg'] = 'I am here'

manager = mp.Manager()
d = manager.dict()

p = mp.Process(target=f, args=(d,))

p.start()
p.join()