#! /usr/bin/python
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import curses
def main(stdscr):
    stdscr.erase()
    stdscr.move(0, 0)
    for i in range(0,stdscr.getmaxyx()[1] - 1):
        stdscr.addstr(".");
    stdscr.addstr(u"\u3007\u3007".encode(code));
    stdscr.refresh()
curses.wrapper(main)