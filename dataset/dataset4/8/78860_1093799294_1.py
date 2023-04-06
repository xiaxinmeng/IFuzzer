import asyncio
import signal
import threading

def mysighandler():
    pass

def do_loop():
    loop = asyncio.new_event_loop()
    # This will fail with RuntimeError: set_wakeup_fd only works in main thread
    loop.add_signal_handler(signal.SIGINT, mysighandler)
    loop.close()

t = threading.Thread(target=do_loop)
t.start()
t.join()