while True:
    evts = poll()
    for evt in evts:
        do_something(fd)