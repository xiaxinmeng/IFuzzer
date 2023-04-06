signal.signal(signal.SIGCHLD, sig_chld_handler)

to_launch = subprocess.Popen("/bin/echo")