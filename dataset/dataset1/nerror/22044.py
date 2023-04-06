import datetime
import random

class TZInfo(datetime.tzinfo):
    def utcoffset(self, datetime):
        return random.random()

def test():
    tz1 = TZInfo()
    dt1 = datetime.datetime(2014, 7, 21, 11, 32, 3, 0, tz1)
    print(dt1.utcoffset())

if __name__ == '__main__':
    test()
