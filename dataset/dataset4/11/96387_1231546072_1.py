import threading
import runtime
import sys

sys.setswitchinterval(0.001)

def calc():
    sum = 0
    for i in range(100000):
        sum += i * i

def daemon_func():
    while True:
        calc()

if __name__ == '__main__':
    threading.Thread(target=daemon_func, name="daemon", daemon=True).start()
    calc()