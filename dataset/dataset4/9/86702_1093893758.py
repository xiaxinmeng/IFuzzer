z = zip([42, []])
item = next(zip)
gc.collect()  # Refcount of item == 2, untracked by GC.
del item  # Refcount of item == 1, ready to be recycled.
next(zip)  # This should be tracked, but won't be.