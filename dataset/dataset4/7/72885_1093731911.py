from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)

def gen():
    yield 1 + '1' # here is an error

print(list(pool.imap(str, gen()))) # prints []
print(list(pool.map(str, gen()))) # raises TypeError