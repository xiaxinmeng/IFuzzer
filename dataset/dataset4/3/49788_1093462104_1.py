def tearDown(self):
    if hasattr(self, 'tmp_io'):
        self.tmp_io.destroy()
    if hasattar(self, 'db'):
        self.db.destroy()