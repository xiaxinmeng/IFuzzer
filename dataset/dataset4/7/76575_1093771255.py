if hasattr(sys, 'getwindowsversion'):
    WIN_MAJOR, _, WIN_BUILD, *_ = sys.getwindowsversion()
    if WIN_MAJOR == 10:
        if WIN_BUILD >= 15063:    # Windows 10 1703
            pass
        elif WIN_BUILD >= 14393:  # Windows 10 1607
            del socket.TCP_KEEPCNT
        else:
            del socket.TCP_KEEPCNT
            del socket.TCP_FASTOPEN
    elif WIN_MAJOR < 10:
        del socket.TCP_KEEPCNT
        del socket.TCP_FASTOPEN