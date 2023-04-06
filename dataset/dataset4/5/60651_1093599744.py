class Nasty(str):
    def __del__(self):
        C.__name__ = "other"
class C(object):
    pass
C.__name__ = Nasty("abc")
C.__name__ = "normal"