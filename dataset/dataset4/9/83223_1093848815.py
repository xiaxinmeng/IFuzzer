import signal
import threading

def int_handler():
   ...

if threading.current_thread() == threading.main_thread():
    signal.signal(signal.SIGINT, int_handler)