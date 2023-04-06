p = multiprocessing.Process(target=C.f, args=(C(),))
p.start()