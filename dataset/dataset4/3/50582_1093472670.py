def setUp(self):
  self.hdlr = logging.StreamHandler(stream)
  someLogger.addHandler(h)

def tearDown(self):
    someLogger.removeHandler(self.hdlr)
    self.hdlr.close()