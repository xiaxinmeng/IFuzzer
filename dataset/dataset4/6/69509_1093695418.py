with ignore_exceptions:
    with ignore_exceptions:  # Check nested usage 
        len(5)
    ignored = True
    1/0
self.assertTrue(ignored)