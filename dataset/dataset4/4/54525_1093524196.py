fileList = tkFileDialog.askopenfilenames(initialdir=self.startfiledir,
                                         title="Select Files for Processing",
                                         filetypes=self.ftypes, multiple=1)