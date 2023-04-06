lock = threading.Lock()

i = 0

def do_loop():
    global i
    for j in range(500000):
        lock.acquire()
        i += 1
        lock.release()


t1 = threading.Thread(target=do_loop)
t2 = threading.Thread(target=do_loop)
t1.start()
t2.start()
t1.join()
t2.join()