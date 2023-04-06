import curses

scr = curses.initscr()
curses.ungetch(1025)
scr.getkey()