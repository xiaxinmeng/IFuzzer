from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)

def gen():
    yield 1
    yield 1 + '1' # here is an error

print(list(pool.imap(str, gen()))) # raises TypeError
print(list(pool.map(str, gen()))) # also would raise TypeError