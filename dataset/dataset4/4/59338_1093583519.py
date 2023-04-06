class MyCheckbutton(Checkbutton):
	def __init__(self, parent, **options):
		Checkbutton.__init__(self, parent, **options)
		self.var = BooleanVar()
		self.configure(indicatoron=False, command=self.cb, variable=self.var)
		print(self.var.get)	# "<bound method BooleanVar.get of <tkinter.BooleanVar object at 0x245c310>>"
		print(self.var.get())	# "0"
	def cb(self, *events): # button callback (manual toggle)
		print(self.var.get)	# <bound method BooleanVar.get of <tkinter.BooleanVar object at 0x245c310>>
		print(self.var.get())	# True