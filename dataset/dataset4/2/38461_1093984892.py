start_time = None
count = 0
delay_ms = 33   # milliseconds

def after_cb():

  f.after(delay_ms, after_cb)