import thread
f=open("tmp1", "w")

def worker():
    global f
    while 1:
        f.close()
        f=open("tmp1", "w")
        f.seek(0,0)

thread.start_new_thread(worker, ())
thread.start_new_thread(worker, ())