import tkinter

def window_size(event):
    if event.delta:   # Windows
        width_window = root.winfo_width() + event.delta // 10
    else:  # Linux
        i = -20
        if event.num == 4:
            i = 20
        width_window = root.winfo_width() + i
    if 250 < width_window < 1000:
        root.geometry(f'{width_window}x{width_window}')

root = tkinter.Tk()
root.resizable(False, False)
root.geometry('400x400')
root.bind_all("<MouseWheel>", window_size)
root.bind_all("<Button-4>", window_size)
root.bind_all("<Button-5>", window_size)
root.mainloop()