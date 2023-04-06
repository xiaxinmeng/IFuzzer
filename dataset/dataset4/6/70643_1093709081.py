import _thread, os, time

def thread1():
    pid = os.fork()
    if not pid:                                            
        # In the child, the original main thread no longer exists. Start a
        # new thread that will stall for 60 s.
        _thread.start_new_thread(time.sleep, (60,))

_thread.start_new_thread(thread1, ())
time.sleep(2)  # Give fork() a chance to run