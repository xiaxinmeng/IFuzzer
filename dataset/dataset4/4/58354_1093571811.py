from tkinter import *

class SelectTest:
    def __init__(self):
        self.mainwin = Tk()
        # Create a text widget
        # idle creates the text widget like this
        #self.text = text = MultiCallCreator(Text)(text_frame, **text_options)
        self.textbox = Text(self.mainwin, width=80, height=10)
        self.textbox.pack()

        # Add some text
        self.textbox.insert(INSERT, "line 1: Select some text\n")
        self.textbox.insert(INSERT, "line 2: Select some text\n")
        self.textbox.insert(INSERT, "line 3: Select some text\n")
        self.textbox.insert(INSERT, "line 4: Select some text\n")

        # Add the binding
        self.textbox.bind("<Control-Key-b>", self.select_just_like_idle)
        # just in case caps lock is on
        self.textbox.bind("<Control-Key-B>", self.select_just_like_idle)
        self.lineno = 1
	
    def select_just_like_idle(self, event):
        print("Select just like idle was called")
        if self.lineno is not None and self.lineno > 0:
            self.textbox.mark_set("insert", "%d.0" % self.lineno)
            self.textbox.tag_remove("sel", "1.0", "end")
            self.textbox.tag_add("sel", "insert", "insert +1l")
            self.lineno = self.lineno + 1


if __name__ == "__main__":
    # Start the program
    selectIDLETest = SelectTest()
    selectIDLETest.mainwin.mainloop()