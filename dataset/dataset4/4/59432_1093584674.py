import Tkinter                    
tk = Tkinter.Tk()
window = Tkinter.Frame(tk)
def onDestroy (event):
  pass
window.bind ("<Destroy>", onDestroy)