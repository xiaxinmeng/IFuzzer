class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sysmodules = sys.modules.copy()
    @classmethod
    def tearDownClass(cls):
        for name in sys.modules:
            del sys.modules[name]
        for name in cls.sysmodules:
            sys.modules[name] = cls.sysmodules[name]