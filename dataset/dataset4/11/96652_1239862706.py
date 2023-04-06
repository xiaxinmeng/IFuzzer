import faulthandler
import signal
import time

faulthandler.register(signal.SIGALRM, chain=True)
signal.alarm(1)
time.sleep(2)
print("exit")