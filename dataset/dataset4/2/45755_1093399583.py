class TestPkg(unittest.TestCase):

    def setUp(self):
        self.root = None
        self.syspath = list(sys.path)
        self.sysmodules = sys.modules.copy()

    def tearDown(self):
        sys.path[:] = self.syspath
        sys.modules.clear()
        sys.modules.update(self.sysmodules)
        del self.sysmodules
        cleanout(self.root)