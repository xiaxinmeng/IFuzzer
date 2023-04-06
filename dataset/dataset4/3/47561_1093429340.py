import _multiprocessing
obj = _multiprocessing.Connection(755)
obj.close()
obj.poll()