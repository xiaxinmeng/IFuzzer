import signal
signal.signal(signal.SIGALRM, lambda x,y: 1)
signal.alarm(1)
import time
time.sleep(0.99)