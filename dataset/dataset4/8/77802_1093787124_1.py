import threading
import traceback
finished = threading.Event()
worked = []
def method():
    try:
        repr(threading.current_thread())
        worked.append(True)
    except:
        traceback.print_exc()
        worked.append(False)
    finally:
        finished.set()
    
import _thread
_thread.start_new_thread(method, ())

finished.wait()
assert worked[0]