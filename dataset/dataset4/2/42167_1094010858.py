import Tkinter
import tkFileDialog

root = Tkinter.Tk()
newPath = tkFileDialog.askopenfilename(
	initialdir = "",
)