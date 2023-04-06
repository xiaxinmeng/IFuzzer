def setUp(self):
    self.tmp_io = TempIO() # raise NameError("no such name TempIO")
    self.db = DataBase()

def tearDown(self):
    self.tmp_io.destroy()
    self.db.destroy()