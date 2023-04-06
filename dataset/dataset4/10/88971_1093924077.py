class TestGetsourceInteractive(unittest.TestCase):
    def tearDown(self):
        mod.ParrotDroppings.__module__ = mod
        sys.modules['__main__'] = self.main