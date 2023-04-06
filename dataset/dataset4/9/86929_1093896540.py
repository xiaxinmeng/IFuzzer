import threading
import warnings

class WarnOnDel(object):
    def __del__(self):
        warnings.warn("oh no something went wrong", UserWarning)

def do_work():
    while True:
        w = WarnOnDel()