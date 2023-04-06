from tkinter import *
import time
        
root = Tk()
root.withdraw()
timer = time.perf_counter
##n = 999
##delay = 1
n=1
delay=337
def tick():
    global n
    if n:
        n -= 1
        root.after(delay, tick)
    else:
        print(timer() - start)

tick()
start = timer()
root.mainloop()