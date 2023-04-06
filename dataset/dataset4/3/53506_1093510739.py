while True:
    if lock.acquire(0):
        lock.tstate = tstate
        return True
    else:
        if detect_circularity():
            return False
        global_lock.release()
        saved = save_tstate()
        yield()
        restore_tstate(saved)
        global_lock.acquire()