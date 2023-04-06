class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sysmodules = sys.modules
        sys.modules = sys.modules.copy()
    @classmethod
    def tearDownClass(cls):
        sys.modules = cls.sysmodules