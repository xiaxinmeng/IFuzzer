import _thread as thread
import time

def start():
	print("Secondary thread ID:", thread.get_ident())
	import threading

print("Main thread ID:", thread.get_ident())
thread.start_new_thread(start, ())
time.sleep(1)