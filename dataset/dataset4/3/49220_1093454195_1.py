def f():
    time.sleep(1.0)  # probably irrelevant to the failure

_thread.start_new(f, ())
### end example ###