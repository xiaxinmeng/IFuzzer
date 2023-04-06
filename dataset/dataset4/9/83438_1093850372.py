
from contextvars import ContextVar, copy_context
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

var: ContextVar[int] = ContextVar('var',default=None)

if __name__ == '__main__':
    
    # ***** This hangs forever *****
    with ProcessPoolExecutor(max_workers=1) as pp:
        ctx = copy_context()
        pp.submit(ctx.run, list)

    # ****** This throws 'cannot pickle Context' # ***** This hangs forever *****
    ctx = copy_context()
    p = Process(target=ctx.run, args=(list,))
    p.start()
    p.join()
