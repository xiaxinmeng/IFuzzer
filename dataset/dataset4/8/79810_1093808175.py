import multiprocessing
tuple(multiprocessing.Pool(4).imap(print, (1, 2, 3)))