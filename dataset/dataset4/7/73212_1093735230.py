# valid for 2016
import time
def check():
    t = time.gmtime()
    print(46*86400*365 + 11*86400 + (t.tm_yday-1)*86400 + t.tm_hour*3600 + t.tm_min*60 + t.tm_sec)
    print(time.time())
    print(time.gmtime(0))
check()