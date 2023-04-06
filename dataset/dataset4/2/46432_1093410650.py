exit = lock.release()
lock.acquire()
try:
    pass
finally:
    exit()