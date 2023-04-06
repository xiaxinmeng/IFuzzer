def sub(pid):
    time.sleep(1)
    os.kill(pid, signal.SIGUSR2)