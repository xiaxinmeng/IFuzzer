import curses


def main(stdscr):
    while True:
        c = stdscr.getch()
        if c == curses.KEY_PPAGE:
            stdscr.addstr('Page Up')
        elif c == curses.KEY_NPAGE:
            stdscr.addstr('Page Down')
        else:
            stdscr.addstr('Another key')

curses.wrapper(main)