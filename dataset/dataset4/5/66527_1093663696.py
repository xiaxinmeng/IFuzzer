def _read():
    s = os.read(r, 1)
    read_results.append(s)
    # The main thread is very likely to be inside the write() syscall now, so interrupt it
    os.kill(os.getpid(), SIGALRM)