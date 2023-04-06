import curses
import locale

locale.setlocale(locale.LC_ALL,"")

def doStuff(stdscr):
  message = "hello わたし!"
  stdscr.addstr(0, 0, message, curses.A_BLINK)
  stdscr.getch() # pauses until a key's hit

curses.wrapper(doStuff)