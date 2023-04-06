import time
import ctypes
import ctypes.util

def measure(cb, iterations):
    start = time.time()
    for i in range(iterations):
        cb()
    end = time.time()
    return (end - start)

def do():
    import ctypes
    import ctypes.util

def dont():
    pass

def run(iterations):
  print("Iterations:", iterations)
  print("A", measure(do, iterations))
  print("B", measure(dont, iterations))

run(1000000)
run(100000000)