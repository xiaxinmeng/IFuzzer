import sys
import builtins

def hook(message):
    if message is None:
        return
    builtins._ = message
    print(ascii(message))

sys.displayhook = hook