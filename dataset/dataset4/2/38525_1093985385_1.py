def handler(signum,frame):
    raise Exception

signal.signal(signal.SIGALRM,handler)
signal.alarm(5)
signal.pause()
signal.alarm(0)