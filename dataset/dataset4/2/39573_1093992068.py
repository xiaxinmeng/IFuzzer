import signal
import re
import time


def main():
    num=28 # need more than 60s on a 2.4Ghz core 2
    r=re.compile("a?"*num+"a"*num)

    signal.signal(signal.SIGALRM, signal.default_int_handler)
    signal.alarm(1)
    stime = time.time()
    try:
        r.match("a"*num)
    except KeyboardInterrupt:
        assert time.time()-stime<3
    else:
        raise RuntimeError("no keyboard interrupt")

if __name__=='__main__':
    main()