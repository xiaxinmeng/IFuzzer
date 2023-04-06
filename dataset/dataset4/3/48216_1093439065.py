def test_mkdir(self):
    self.assertRaises(WindowsError, os.chdir, test_support.TESTFN)
def test_access(self):
    self.assertRaises(WindowsError, os.utime, test_support.TESTFN, 0)
def test_chmod(self):
    self.assertRaises(WindowsError, os.utime, test_support.TESTFN, 0)