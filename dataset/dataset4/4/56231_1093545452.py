manager = ThreadTransactionManager()
__enter__ = manager.get
__exit__ = manager.__exit__