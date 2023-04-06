from idlelib import query
from tkinter import Tk
root = Tk()
name = query.Query(root, "Open Module",
         "Enter the name of a Python module\n"
         "to search on sys.path and open:",).result
print(name)