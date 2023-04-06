# test2.py
# Broke it with KeyboardInterrupt
import curses
def main2(screen):
    try:
        k = screen.getkey()
    except KeyboardInterrupt:
        raise
curses.wrapper(main2)
# Terminal is restored to its normal state.