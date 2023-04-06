import curses as cs
def report(stdscr):
    print('press the keypad 5')
    global result
    result=stdscr.getch()
cs.initscr()
cs.wrapper(report)
print('KEY_B2 (decimal): '+str(cs.KEY_B2))
print('input decimal value: '+str(result))