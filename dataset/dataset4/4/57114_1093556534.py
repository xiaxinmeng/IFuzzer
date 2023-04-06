s = signal.SIGALRM
signal.signal(s, lambda x,y: 1/0)
signal.alarm(1)
signal.siginterrupt(s, True)
sys.stdin.read()