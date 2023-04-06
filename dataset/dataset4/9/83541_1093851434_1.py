from multiprocessing import Pool
class A:
    def __init__(self):
        self.pool = Pool(processes=1)
def test():
    problem = A()
    problem.pool.map(float, tuple(range(10)))
if __name__ == "__main__":
    test()