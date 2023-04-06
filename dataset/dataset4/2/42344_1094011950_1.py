def shutdown():
    for i in range(len(_handlers)):
        for h in _handlers.keys():
            h.flush()
    for h in _handlers.keys():
        h.close()