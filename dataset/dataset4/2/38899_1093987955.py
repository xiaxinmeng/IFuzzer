import Tkinter
tk = Tkinter.Tk()
quit_btn = Tkinter.Button(tk, text='quit', 
                          #command=tk.quit)  # This crashes
                          command=tk.destroy)  # This works
       
quit_btn.pack()
Tkinter.mainloop()