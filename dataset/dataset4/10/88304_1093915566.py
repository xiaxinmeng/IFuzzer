
import multiprocessing
import os
import signal

lk = multiprocessing.Lock()

def f():
    my_pid = os.getpid()
    print("PID {} going to wait".format(my_pid))
    with lk:
        print("PID {} got the lock".format(my_pid))
        os.kill(my_pid, signal.SIGKILL)

if __name__ == '__main__':
    for i in range(5):
        multiprocessing.Process(target=f).start()
