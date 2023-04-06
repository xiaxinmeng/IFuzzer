def start_color():
    import _curses, curses  
    # This import is from the initscr() wrapper
    val = _curses.start_color()

    if _curses.__dict__.has_key('COLOR_PAIRS'):
        curses.COLOR_PAIRS = _curses.COLOR_PAIRS
    if _curses.__dict__.has_key('COLORS'):
        curses.COLORS = _curses.COLORS

    return val