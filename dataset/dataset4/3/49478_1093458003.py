from multiprocessing import Pool

def power (x, pwr=2):
    return x**pwr

import functools
run_test = functools.partial (power, pwr=3)

if __name__ == "__main__":

    pool = Pool()
    cases = [3,4,5]
    results = pool.map (run_test, cases)