import multiprocessing
import os

def do(i):
      print(test_forkserver(), os.getpid())

def test_forkserver():
      mp = multiprocessing.get_context('forkserver')
      mp.Pool(2).map(do(mp), range(3))
if __name__ == '__main__':
      test_forkserver()