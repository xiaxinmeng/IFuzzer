class TestA(unittest.TestCase):

  def setUp():
    patcher = mock.patch.object(...)
    self.mock_a = patcher.start()
    self.addCleanup(patcher.stop)