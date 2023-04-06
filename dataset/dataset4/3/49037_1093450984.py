import curses
import locale

locale.setlocale(locale.LC_ALL,"")

def doStuff(stdscr):
  message = u"hello わたし!"
  stdscr.addstr(0, 0, message.encode("utf-8"), curses.A_BLINK)
  stdscr.getch() # pauses until a key's hit

curses.wrapper(doStuff)