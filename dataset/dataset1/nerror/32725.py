import _multiprocessing

class BadPipeConnection(_multiprocessing.PipeConnection):
    pass

x = BadPipeConnection(0)
del x
