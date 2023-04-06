class TestFoo(TestCase):
  def checkFoo(self):   
   dirname = self.getPath()
   # or
   filename = self.getPath("foo.data")