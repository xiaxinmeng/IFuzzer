tracemalloc_filters = [
   tracemalloc.Filter(False, '<frozen importlib._bootstrap>', all_frames=True),
   tracemalloc.Filter(False, tracemalloc.__file__, all_frames=True),
]