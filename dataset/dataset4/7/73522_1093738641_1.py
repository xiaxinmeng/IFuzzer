print(tracemalloc.get_traced_memory())
allobj = sys.getobjects(0, tuple)
print(len(allobj))