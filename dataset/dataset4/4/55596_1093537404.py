class App():  
    def __init__(self):
        self.root = tk.Tk()
        
        self.btn = tk.Button(self.root, text='Click me')
        self.btn.pack()
        self.btn.bind('<Button-1>', self.click)

        self.root.mainloop()
        
    def click(self, event):
        # Messagebox or filedialog
        pass