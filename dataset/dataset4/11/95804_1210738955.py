h.aqcuire()
if not isinstance(h, MemoryHandler):
    h.flush()
h.close()