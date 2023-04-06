import multiprocessing

def f(x):
    return 0;

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2,maxtasksperchild=1);
    results = list();
    for i in range(10):
        results.append(pool.apply_async(f, (i)));
    pool.close();
    pool.join();
    for r in results:
        print(r);
    print("Done");