import _tkinter, subprocess
print(subprocess.getoutput("otool -L " + _tkinter.__file__))
print(subprocess.getoutput("ls -l /Library/Frameworks/Tk.framework/Versions"))