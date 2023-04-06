import sys
from multiprocessing import Pool


class Failure:
    def __reduce__(self):
        return sys.exit, (0, )


pool = Pool(2)
pool.apply(id, (Failure(),))