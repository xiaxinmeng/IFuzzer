import multiprocessing

def the_test():
    pool = multiprocessing.Pool(1)
    with pool:
        print(pool.apply(int, (2,)))
    with pool:
        print(pool.apply(int, (3,))) # <-- raise here

the_test()