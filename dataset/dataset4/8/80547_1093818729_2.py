class TestB(TestA):

  def setUp():
    super().setUp()
    self.addCleanup(mock.patch.stopall)
    self.mock_b = mock.patch.object(...).start()