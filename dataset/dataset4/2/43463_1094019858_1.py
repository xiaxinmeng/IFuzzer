screen = curses.initscr()

screen.addstr("\x80")

screen.getch()
curses.endwin()