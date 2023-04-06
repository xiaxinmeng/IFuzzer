#!/usr/bin/python
import curses
from curses.textpad import Textbox

def main(stdscr):
    box = Textbox(stdscr, insert_mode=True)
    box.stripspaces = True
    while 1:
        cmd = box.edit()
        if cmd == 'q':
            break

curses.wrapper(main)