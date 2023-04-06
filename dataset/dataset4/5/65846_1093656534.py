import unicode
from test.support import requires
try:
    requires('gui')
    from tkinter import Tk, Text
    running_gui = True
except unicode.SkipTest:
    from idlelib.idle_test.mock_tk import Text
    running_gui = False