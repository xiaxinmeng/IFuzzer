
import tkinter as tk

root = tk.Tk()

labels = []
for i in range(3):
    label = tk.Label(root)
    label.grid(row=0, column=i)
    labels.append(label)
