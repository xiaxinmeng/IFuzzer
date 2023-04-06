import sys, threading

def _thread():
    data = sys.stdin.buffer.readline()

thread = threading.Thread(target=_thread)
thread.daemon = True
thread.start()