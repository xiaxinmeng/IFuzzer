class Test(object):
    def __init__(self):
        self.__private = "Hello"
    def test(self):
        print(self.__private)
        print(hasattr(self, "__private"))
        print(getattr(self, "__private"))


t = Test()
t.test()