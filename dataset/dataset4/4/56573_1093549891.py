import concurrent.futures
import faulthandler
import os
import signal
import time

def work(n):
    time.sleep(0.1)

def main():
    faulthandler.register(signal.SIGUSR1)
    print("pid: %s" % os.getpid())
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in executor.map(work, range(100)):
            print("shutdown")
            executor.shutdown()
            print("shutdown--")

if __name__ == '__main__':
    main()