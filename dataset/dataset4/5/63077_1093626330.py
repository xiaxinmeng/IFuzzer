import tkinter 
import tkinter.filedialog  

def callback():
    name = tkinter.filedialog.askopenfilenames() 
    print(name)
     
tkinter.Button(text='File Open', command=callback).pack()
tkinter.mainloop()