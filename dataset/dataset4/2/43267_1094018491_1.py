import _tkinter, os
if "DISPLAY" in os.environ: del os.environ["DISPLAY"]
tk = _tkinter.create(None, "test", "Tk", 0, 1, 0)
try: tk.loadtk()
except: pass
tk.loadtk()