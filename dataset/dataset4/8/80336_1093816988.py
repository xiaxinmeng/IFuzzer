self.assertIn(l, gc.get_objects(generation=0))
self.assertNotIn(l, gc.get_objects(generation=1))
self.assertNotIn(l, gc.get_objects(generation=2))