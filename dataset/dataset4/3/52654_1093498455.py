pthread_sigmask(SIG_BLOCK, [SIGUSR1])
os.kill(os.getpid(), SIGUSR1)
pthread_sigmask(SIG_UNBLOCK, [SIGUSR1])