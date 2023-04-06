import curses
from curses import panel
def mkpanel(scr):
        win = curses.newwin(8,8,1,1)
        pan = panel.new_panel(win)
curses.wrapper(mkpanel)