import curses

def test_screen(screen):
    screen.nodelay(True)
    key = screen.getch()
    screen.nodelay(False)
    curses.ungetch(key)

curses.wrapper(test_screen)