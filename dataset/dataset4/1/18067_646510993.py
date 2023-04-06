
try:
    with self.assertNoLogs(...) as watcher:
        ...
except AssertionError:
    # do something with the nonempty watcher, probably provide a different failure message.
    self.fail(...)
