for n in range(0,100000):
    if n % 100 == 0:
        sys.stdout.write("%d" % n)
        sys.stdout.flush()
    pid = os.fork()
    if pid != 0:
        os.wait()
    else:
        os._exit(0)