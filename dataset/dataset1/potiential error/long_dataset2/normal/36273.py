import threading

def recurse():
    return recurse()

def outer():
    try:
        recurse()
    except RecursionError:
        print("outer: RecursionError")

w = threading.Thread(target=outer)
w.start()
w.join()
print('end of main thread')
