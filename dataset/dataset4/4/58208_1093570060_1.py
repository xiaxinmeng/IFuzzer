if pid == 0:
    # Child
    os.execv("/usr/bin/ssh", args)