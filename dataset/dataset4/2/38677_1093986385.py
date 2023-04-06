import signal
import thread
import os

def handle_signals(sig, frame): pass
def send_signals(): os.kill(os.getpid(), signal.SIGSEGV)

signal.signal(signal.SIGSEGV, handle_signals)
thread.start_new_thread(send_signals, ())
signal.pause()