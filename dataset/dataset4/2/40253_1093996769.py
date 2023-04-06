def readwrite(obj, flags):
    try:
        if flags & (select.POLLIN | select.POLLPRI):
            obj.handle_read_event()
        if flags & select.POLLOUT:
            obj.handle_write_event()
        if flags & (select.POLLERR | select.POLLHUP |
select.POLLNVAL):
            obj.handle_expt_event()
    except ExitNow:
        raise
    except:
        obj.handle_error()