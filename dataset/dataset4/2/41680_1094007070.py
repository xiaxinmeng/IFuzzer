if flags & select.POLLPRI:
    obj.handle_expt_event()
if flags & select.POLLIN:
    obj.handle_read_event()
if flags & select.POLLOUT:
    obj.handle_write_event()
if flags & (select.POLLERR | select.POLLNVAL | select.POLLHUP):
    obj.handle_close()