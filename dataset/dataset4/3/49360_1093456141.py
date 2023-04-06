import sys
import builtins

def hook(message):
    if message is None:
        return
    builtins._ = message
    try:
        print(repr(message))
    except UnicodeEncodeError:
        print(ascii(message))

sys.displayhook = hook