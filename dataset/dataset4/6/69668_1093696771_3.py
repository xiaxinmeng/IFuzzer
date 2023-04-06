signal.set_wakeup_fd(wfd)

signal.signal(signal.SIGWINCH, lambda *args:0)
select.select([rfd], [], [])
print(os.read(rfd, 2))