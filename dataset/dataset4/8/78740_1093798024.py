import multiprocessing.managers
a = multiprocessing.managers.SyncManager(authkey=b'')
a.start()
b = a.list()
b.append(a.list())
_ = b[0]