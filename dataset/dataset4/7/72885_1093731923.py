import multiprocessing.pool

def gen():
    raise Exception('generator exception')
    yield 1
    yield 2

for i in range(3):
    with multiprocessing.pool.ThreadPool(3) as pool:
        try:
            print(list(pool.imap_unordered(lambda x: x*2, gen())))
        except Exception as e:
            print(e)