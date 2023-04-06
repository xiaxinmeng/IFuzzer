import resource

l = [0, 0]

class MyNum:
    def __int__(self):
        l[1] = 20
        return 10

    def __del__(self):
        print('byebye', self)

l[0] = MyNum()
l[1] = MyNum()
resource.setrlimit(resource.RLIMIT_CPU, l)
