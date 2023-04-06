import rlcompleter
import curses
f = open('mytempfile', 'w+b')
stdscr = curses.initscr()
stdscr.putwin(f)
f.seek(0)
curses.getwin(f)
f.close()
curses.endwin()