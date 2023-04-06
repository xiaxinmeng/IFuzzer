import curses

scr = curses.initscr()
try:
    char = scr.get_wch()
except KeyboardInterrupt:
    pass