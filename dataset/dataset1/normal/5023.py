from datetime import time, timedelta, tzinfo

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(minutes=offset)
    def utcoffset(self, dt):
        return self.__offset

def test_zones():
    t3 = time(13, 47, tzinfo=FixedOffset(60))
    print (t3.strftime("%z") == "+0100")

if __name__ == "__main__":
    test_zones()
