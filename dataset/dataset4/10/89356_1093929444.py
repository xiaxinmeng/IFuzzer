TK_VERSION = tuple(map(int, tk.call("info", "patchlevel").split(".")))
if (8, 6, 8) <= TK_VERSION < (8, 6, 10):
    acw.update_idletasks()