from multiprocessing import Process, current_process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    if not hasattr(os, 'getppid'):  # win32
      print('parent process:', current_process()._parent_pid)
    else:
      print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()