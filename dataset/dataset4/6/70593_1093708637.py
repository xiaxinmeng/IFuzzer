import tkinter as tk
from tkinter import filedialog, ttk

class MainWindow(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.pack()
        btnoptions = {'expand':True, 'fill': 'both'}
        btn = ttk.Button(self, text='Select', command=self.ask_openfile)
        btn.pack(**btnoptions)

    def ask_openfile(self):
        filename = filedialog.askopenfilename()
        return filename

if __name__=='__main__':
    root = tk.Tk()
    root.geometry('600x300')
    MainWindow(root).pack(expand=True, fill='both', side='top')
    root.mainloop()