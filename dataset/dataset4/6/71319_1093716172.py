def assertSuperset(self, superset, subset):
    # Expand for friendlier failure handling
    self.assertTrue(all(e in superset for e in subset))

self.assertSuperset("Error message", ("mess", "or me"))