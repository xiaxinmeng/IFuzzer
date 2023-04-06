import Tkinter, subprocess, _tkinter
Tkinter.Tcl().eval('info patchlevel')
print(subprocess.check_output(["otool", "-L", _tkinter.__file__]))