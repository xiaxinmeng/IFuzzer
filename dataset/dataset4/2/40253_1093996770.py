if flags & (select.POLLERR | select.POLLNVAL):
    obj.handle_expt_event()
if flags & select.POLLHUP:
    obj.handle_close_event()