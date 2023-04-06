
def test_stuff(self):
   self.addTypeEqualityFunc(
      MyObject,
      comparison_method_which_compares_how_i_want,
   )
   self.assertListEqual(
      get_list_of_objects(),
      [MyObject(...), MyObject(...)],
   )
