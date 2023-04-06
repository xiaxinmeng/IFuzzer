import sys, os
import multiprocessing as mp

if __name__ == '__main__':
    p = mp.Pool(4, maxtasksperchild=5)
    results = []

    for i in range(100):
        if i % 10 == 0:
            results.append(p.apply_async(sys.exit))
        else:
            results.append(p.apply_async(os.getpid))

    for i, res in enumerate(results):
        if i % 10 != 0:
            print(res.get())
        else:
            pass      # trying res.get() would block forever