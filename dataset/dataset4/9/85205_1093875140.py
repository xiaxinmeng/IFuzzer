
import os, readline, signal, sys

del sys.modules["readline"]
import readline

os.kill(os.getpid(), signal.SIGWINCH)
