class Example(TestCase):
 def setUp(self):
  self._1 = acquire()
  self.addCleanUp(acquire())
  self._3 = acquire()

 def tearDown(self):
  self._3.cleanUp()
  self._1.cleanUp()
  super().tearDown()