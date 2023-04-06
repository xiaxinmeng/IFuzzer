import traceback

class Err(Exception):
    def __del__(self):
        print("del")

def raise_exc(exc):
    raise exc

e = Err()
try:
    raise_exc(e)
except Exception as e:
    t = e.__traceback__
#traceback.clear_frames(t)
e = None
print("exit")