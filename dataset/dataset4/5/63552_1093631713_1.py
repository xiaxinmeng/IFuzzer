if hasattr(resource, 'RLIMIT_NICE'):
    self.assertTrue(-20 <= resource.RLIMIT_NICE <= 19)