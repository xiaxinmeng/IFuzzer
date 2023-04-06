import multiprocessing
import sys
def test(value):
    if value:
        sys.exit(123)
if __name__ == '__main__':
    pool = multiprocessing.Pool(4)
    cases = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    pool.map(test, cases)