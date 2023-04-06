# test.py
# Broke it with KeyboardInterrupt
import curses
def main(screen):
    k = screen.getkey()
curses.wrapper(main)
# Results are hardly readable due to the broken terminal.
# Something about KeyboardInterrupt