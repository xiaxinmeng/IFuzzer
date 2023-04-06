import ctypes, sys, time, thread

# Module globals are cleared before __del__ is run
# So save the functions in class dict
class C:
    ensure = ctypes.pythonapi.PyGILState_Ensure
    release = ctypes.pythonapi.PyGILState_Release
    def __del__(self):
        state = self.ensure()
        self.release(state)

def waitingThread():
    x = C()
    time.sleep(100)

thread.start_new_thread(waitingThread, ())
time.sleep(1)
sys.exit(42)