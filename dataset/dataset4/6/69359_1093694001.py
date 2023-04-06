tk = import_module('tkinter')  # Also imports _tkinter.
if tk.TkVersion < 8.5:
    raise unittest.SkipTest("IDLE requires tk 8.5 or later.")