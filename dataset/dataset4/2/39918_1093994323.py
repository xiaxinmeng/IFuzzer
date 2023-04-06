import curses;

stdscr = curses.initscr();
curses.raw();
curses.noecho();
stdscr.keypad(1);