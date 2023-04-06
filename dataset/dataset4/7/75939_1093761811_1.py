refcount_before = sys.gettotalrefcount()
elem.__setstate__({'tag': 42, '_children': []})
print(sys.gettotalrefcount() - refcount_before)  # should be close to -1000