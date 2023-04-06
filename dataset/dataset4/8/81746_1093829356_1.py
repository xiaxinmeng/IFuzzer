
import faulthandler, signal, os

def handler(signum, frame):
    handler.called = True
handler.called = False

faulthandler.enable()

signum = signal.SIGUSR1
signal.signal(signum, handler)
faulthandler.register(signum, chain=True)
os.kill(os.getpid(), signum)
print("called", handler.called)
