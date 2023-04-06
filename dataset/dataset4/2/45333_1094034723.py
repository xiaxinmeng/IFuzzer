while 1:
    f = open("/tmp/dupa", "w")
    thread.start_new_thread(f.close, ())
    f.close()