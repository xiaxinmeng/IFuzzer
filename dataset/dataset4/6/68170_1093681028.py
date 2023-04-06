root = tk.Tk()

tcl_ver = tk.TclVersion  # Typical but low precsion
tcl_ver = tk.Tcl().eval('info patchlevel')  # Works but uses eval()
tcl_ver = root.tcl.call('info', 'patchlevel')  # Fails (AttributeError)
tcl_ver = tk.Tcl().call('info', 'patchlevel')  # Works, using

tk_ver = tk.TkVersion  # Typical but low precsion
tk_ver = tk.Tk().eval('info patchlevel')  # Works but makes extra window, uses eval()
tk_ver = tk.Tk().call('info', 'patchlevel')  # Works but makes extra window
tk_ver = root.tk.call('info', 'patchlevel')  # Works, using