import curses, signal, time, sys

def sigwinch (signum, frame): return

win = curses.initscr ()

signal.signal(signal.SIGWINCH, sigwinch)

while 1: win.getkey ()