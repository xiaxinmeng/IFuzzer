

import signal

def sig_hdlr(signum, frame):
    raise ValueError()

def faulty():
    local_var = ""
    signal.signal(signal.SIGALRM, sig_hdlr)
    signal.alarm(1)
    try:
        while True:
            local_var += "!"
    except ValueError:
        print (local_val)

faulty()
