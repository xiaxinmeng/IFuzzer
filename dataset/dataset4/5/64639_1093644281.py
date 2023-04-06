class Nasty(str):
    def __del__(self):
        C.__qualname__ = "other"

class C:
    pass

C.__qualname__ = Nasty("abc")
C.__qualname__ = "normal"
C.__qualname__ = "normal"