import gc, json

class leak(object):
    def __init__(self):
        pass

gc.set_debug(gc.DEBUG_LEAK)
while True:
    leak_ = leak()
    json.dumps(leak_.__dict__, indent=True)
    gc.collect()
    print(f"garbage count: {len(gc.garbage)}")