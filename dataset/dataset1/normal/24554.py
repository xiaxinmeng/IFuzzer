class C(object):
    pass

class Pool(object):
    def __del__(self):
        print('del')
        list()

C.pool = Pool()
