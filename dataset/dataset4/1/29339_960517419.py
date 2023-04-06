# Verify distinct results for equivalent tuples with differing types
cached_repr = self.module.lru_cache(maxsize=maxsize, typed=True)(repr)
self.assertEqual(cached_repr((True, 'string')), "(True, 'string')")
self.assertEqual(cached_repr((1, 'string')), "(1, 'string')")