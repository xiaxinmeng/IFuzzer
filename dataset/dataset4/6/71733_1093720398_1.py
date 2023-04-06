def update():
    while(do_one_event(sleep_ok=False)): pass

def mainloop():
    while toplevels and not stop:
        do_one_event()