def walk_wrapper(walk_it):
    for dir_entry in walk_it:
        if dir_entry.dirpath == "aaa":
           yield dir_entry