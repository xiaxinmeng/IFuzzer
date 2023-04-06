# child process
if pid == 0:
    os.setsid()
    os.close(master)

    os.dup2(slave, 0)
    os.dup2(slave, 1)
    os.dup2(slave, 2)

    max_fd = resource.getrlimit(resource.RLIMIT_NOFILE)[0]
    os.closerange(3, max_fd)

    # make controlling terminal.  taken from pty.fork
    tmp_fd = os.open(os.ttyname(1), os.O_RDWR)
    os.close(tmp_fd)

    os.write(1, "testing".encode())

    os._exit(255)