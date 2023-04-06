from Tkinter import *
import tkMessageBox

class App(Frame):
  def __init__(self, master):
    Frame.__init__(self,master)
    self.master.title("Wierd Menu")
    self.configure(height=200,width=200)
    self.grid(padx=15, pady=15,sticky=N+S+E+W)       
    self.menu = Menu(self)
    self.master.config(menu=self.menu)
    self.tkMenu = Menu(self.menu)
    self.menu.add_cascade(label="MenuItem", menu=self.tkMenu)
    self.tkMenu.add_command(label="Test", command=self.Test)
  def Test(self):
    tkMessageBox.showinfo("Test", "Test")
if __name__ == "__main__":
  root = Tk()
  app = App(root)
  root.mainloop()