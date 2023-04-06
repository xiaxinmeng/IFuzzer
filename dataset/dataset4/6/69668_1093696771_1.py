signal.set_wakeup_fd(wfd)
select.select([rfd], [], [])
print(os.read(rfd, 2))