import threading
import sys

def f(n=0):
    try:
        print(n)
        f(n+1)
    except Exception:
        print("we hit recursion limit")
        sys.exit(0)

t = threading.Thread(target=f)
t.start()
