from multiprocessing import Pool
def double(x):
    return 2 * x
class buggy:
        def __iter__(self):
                return self
        def __next__(self):
                raise Exception('oops')
        def __len__(self):
                return 1
list(Pool(processes=2).map(double, buggy()))
list(Pool(processes=2).map(double, buggy()))  # hangs