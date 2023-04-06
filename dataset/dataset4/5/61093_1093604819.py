import logging, unittest

log = logging.getLogger()

class Test(unittest.TestCase):
    def setUp(self):
        log.info("setting up")
    def test1(self):
        pass
    def test2(self):
        pass

logging.basicConfig(level=logging.INFO)
unittest.main()