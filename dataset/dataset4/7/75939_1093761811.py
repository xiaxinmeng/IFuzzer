refcount_before = sys.gettotalrefcount()
parser.__init__(target=builder)
print(sys.gettotalrefcount() - refcount_before)  # should be close to 0