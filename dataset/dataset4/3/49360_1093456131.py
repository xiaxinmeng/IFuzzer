import sys

def hook(message):
    print(ascii(message))

sys.displayhook = hook