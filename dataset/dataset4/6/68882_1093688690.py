class Base(TestCase):

 def setUp(self):
  super().setUp()
  self.helper = Something()

 def tearDown(self):
  self.helper.finished()
  self.helper = None
  super().tearDown()


class Child(Base):

 def setUp(self):
  super().setUp()
  self.addCleanup(self.helper.release, my_resource)