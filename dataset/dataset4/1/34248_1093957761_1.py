import sys

def start_color():
    # If this code gets called, then these modules are guaranteed to exist:
    curses = sys.module['curses']
    _curses = sys.module['_curses']

    val = _curses.start_color()
    
    if _curses.__dict__.has_key('COLOR_PAIRS'):
        curses.COLOR_PAIRS = _curses.COLOR_PAIRS
    if _curses.__dict__.has_key('COLORS'):
        curses.COLORS = _curses.COLORS

    return val