
import signal
import threading
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
t = threading.Thread(target=kernel32.CtrlRoutine, args=(signal.CTRL_C_EVENT,))
t.start()
t.join()
