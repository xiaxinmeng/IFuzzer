import tkinter as tk
from idlelib.configdialog import ConfigDialog
from idlelib import macosx

_realsetup = tk.BaseWidget._setup
def _wrapsetup(self, master, cnf):
    _realsetup(self, master, cnf)
    print(self.widgetName, self._w)
tk.BaseWidget._setup = _wrapsetup

root = tk.Tk()
macosx._initializeTkVariantTests(root)
ConfigDialog(root)
tk.BaseWidget._setup = _realsetup