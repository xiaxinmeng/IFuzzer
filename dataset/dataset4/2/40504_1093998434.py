#!/usr/bin/python
import curses, sys

def init_display(stdscr):
    stdscr.clear()
    stdscr.refresh()
    size = stdscr.getmaxyx()
    sys.stderr.write("Now %u x %u\n" % (size[1],size[0]))
    rootwin = stdscr.derwin(20, 50, 0, 0)
    return rootwin

def main(stdscr):
    rootwin = init_display(stdscr)
    while 1:
        input = rootwin.getch()
        if ( input == curses.KEY_RESIZE):
            init_display(stdscr)
        elif input == ord("q"):
            sys.exit()
        rootwin.refresh()

curses.wrapper(main)