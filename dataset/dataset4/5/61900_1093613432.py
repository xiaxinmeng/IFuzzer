import curses

def main(stdscr):
    stdscr.addstr(0,0, "Key")
    stdscr.refresh()
    curses.ungetch(0x0149)
    while True:
        ch = stdscr.get_wch()
        stdscr.addstr(1,1, repr(ch) + '      ')
        if ch == 'q':
            break
        
curses.wrapper(main)