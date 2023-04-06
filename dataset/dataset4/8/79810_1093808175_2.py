with contextlib.closing(multiprocessing.Pool(jobs)) as pool:
    tuple(pool.imap(...))