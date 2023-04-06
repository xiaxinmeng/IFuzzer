import time
from tkinter import Tk
root = Tk()

while True:
    root.update()  # Huge memory leak

while True:
    root.update()  # No memory leaks
    time.sleep(1)