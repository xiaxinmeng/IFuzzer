class BaseRobotTest:
    def setUp(self):
        lines = io.StringIO(robots_txt).readlines()
        self.parser = urllib.robotparser.RobotFileParser()
        parser.parse(lines)

    def test_good(self):
         for url in good:
             self.assertTrue(self.parser.can_fetch(...))

    def test_bad(self):
         for url in bad:
             self.assertFalse(self.parser.can_fetch(...))

class RobotTestX(BaseRobotTest, unittest.TestCase):
    doc = "..."
    good = [...]
    bad = [...]