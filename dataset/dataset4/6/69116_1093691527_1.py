@patch.dict(foo, OrderedDict(update_values))
def test():
    self.assertEqual(list(foo), sorted(foo))

test()