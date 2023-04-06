class A(TestCase):
 def setUp(self):
  super().setUp()
  acquire1()

class B(A):
 def setUp(self):
  acquire2()
  super().setUp()

class C(B):
 def setUp(self):
  super().setUp()
  acquire3()