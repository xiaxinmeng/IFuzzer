import curses

def test(stdscr):
    stdscr.addch(0, 5, b'R')
    stdscr.addch(5, 0, b'B')
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(test)