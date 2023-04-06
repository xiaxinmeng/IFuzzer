import curses

def init_curses():
    curses.initscr()
    window = curses.newwin(curses.LINES - 1, curses.COLS, 0, 0)