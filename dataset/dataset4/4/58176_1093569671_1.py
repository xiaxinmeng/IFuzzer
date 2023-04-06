def globtree(*patterns, **kwds):
    kwds.setdefault("top", ".")
    return file_paths(filtered_walk(included_files=patterns, **kwds))