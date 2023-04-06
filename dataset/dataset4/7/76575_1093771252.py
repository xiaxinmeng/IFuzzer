if hasattr(sys, 'getwindowsversion') and sys.getwindowsversion()[0] < 10:
    del socket.TCP_KEEPCNT
    del socket.TCP_FASTOPEN