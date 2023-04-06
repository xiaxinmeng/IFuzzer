import Tkinter as tk
root=tk.Tk()

def scollEntry(*args):
   if args[0]=='scroll':
        e.xview_scroll(args[1],args[2])
   if args[0]=='moveto':
        e.xview_moveto(args[1])

e=tk.Entry(width=10)
e.grid(row=0, sticky='e'+'w')

s=tk.Scrollbar(orient='horizontal')
s.grid(row=1, sticky='e'+'w')