from multiprocessing import Process
import dbm

db = dbm.open("example.dbm", "c")
for i in range(100):
    db[str(i)] = str(i ** 2)


def parallel():
    for i in range(100):
        print(db[str(i)])

a = Process(target = parallel)
b = Process(target = parallel)
a.start()
b.start()
a.join()
b.join()