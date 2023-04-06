import curses

def test_screen(screen):
    screen.addch(5,5, curses.ACS_HLINE)
    screen.refresh()

curses.wrapper(test_screen)