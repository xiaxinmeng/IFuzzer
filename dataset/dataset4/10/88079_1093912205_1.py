unittest.addModuleCleanup(print, 'module cleanup')

class Dummy(unittest.TestCase):
    def test_dummy(self):
        self.addCleanup(print, 'test cleanup')
        self.addClassCleanup(print, 'class cleanup')

unittest.main()