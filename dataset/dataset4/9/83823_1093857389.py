self.printBtn = tkinter.Button(self.frame, text='Print')
self.printBtn['state'] = tkinter.DISABLED
self.printBtn.bind(sequence='<Button-1>', func=self.printBtn_onclick)
self.printBtn.pack()