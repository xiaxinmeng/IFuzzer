class Test(object):
    def __init__(self, a={}):
        self._a = a
    
    def put(self, k, v):
        self._a[k] = v

if __name__ == '__main__':
    t1 = Test()
    t1.put('aa', '11')
    t1.put('bb', '22')
    
    t2 = Test()
    t2.put('cc', '33')
    for k, v in t2._a.items():
        print(k, '=', v)