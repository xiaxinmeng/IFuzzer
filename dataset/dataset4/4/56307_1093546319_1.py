def myfunc(x):
    import sys
    print("child", os.getpid(), "optimize?", sys.flags.optimize)
    assert False, "assert False"
    return x

if __name__ == '__main__':
    import sys
    print("parent optimize?", sys.flags.optimize)
    pool = Pool(processes=2)
    pool.map(myfunc, xrange(2)) # or imap_unordered, map