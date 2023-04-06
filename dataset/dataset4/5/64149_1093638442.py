import unittest

class A(unittest.TestCase):
   def __init__(self, *args, **kwargs):
       print('called only once!')
       super().__init__(*args, **kwargs)

   def test(self):
       self.assertEqual(1, 1)
 
   def test2(self):
       self.assertEqual(2, 2)

if __name__ == '__main__':
   unittest.main()