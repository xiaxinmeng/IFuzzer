def readwrite(obj, flags):
    try:
        if flags & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            obj.handle_close()
        else:
            if flags & select.POLLIN:
                obj.handle_read_event()
            if flags & select.POLLOUT:  # and obj.connected:
                obj.handle_write_event()
            if flags & select.POLLPRI:  # and obj.connected:
                obj.handle_expt_event()
    except _reraised_exceptions:
        raise
    except:
        obj.handle_error()