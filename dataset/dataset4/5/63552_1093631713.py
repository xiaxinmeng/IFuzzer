if hasattr(resource, 'RLIMIT_NICE'):
    self.assertIsInstance(resource.RLIMIT_NICE, int)