import curses
import time

def display(screen):
    while 1:
        screen.erase()
        screen.addstr("1234567012345670\n")
        screen.addstr("       012345670\n")
        screen.refresh()

        time.sleep(100)
                        
curses.wrapper(display)