def handler(signum, frame):
    print('Signal handler called with signal %s' % signum)

# Set the signal handler and a 1-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

# We should not actually sleep for 10 seconds
time.sleep(10)
signal.alarm(0)