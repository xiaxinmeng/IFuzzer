def initscr():
    import _curses, curses
    # we call setupterm() here because it raises an error
    # instead of calling exit() in error cases.
    setupterm(term=_os.environ.get("TERM", "unknown"),
              fd=_sys.__stdout__.fileno())
    stdscr = _curses.initscr()
    for key, value in _curses.__dict__.items():
        if key[0:4] == 'ACS_' or key in ('LINES', 'COLS'):
            setattr(curses, key, value)

    return stdscr