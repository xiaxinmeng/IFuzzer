def do_one_event(sleep_ok):
    if ready:
        process(ready.pop())
        return True
    load_ready()
    if ready:
        process(ready.pop())
        return True
    if idle:
        for event in idle:
            process(event)
        return True
    if sleep_ok:
        sleep_until_event()  # the hard part
        load_ready()
        process(ready.pop())
        return True
    else:
        return False

def load_ready():
    # In some unspecified order
    ready.extend(get_window_events)  # graphics system
    ready.extend(get_file_events)  # select
    ready.extend(get_timer_events)  # priority queue pops