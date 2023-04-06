with self.assertWarns(DeprecationWarning) as w:
    Foo('test_func').run()
self.assertIn('It is deprecated to return a value!=None', w.warnings[0].message)
self.assertIn('test_func', w.warnings[0].message)
self.assertEqual(w.warnings[0].filename, __file__)