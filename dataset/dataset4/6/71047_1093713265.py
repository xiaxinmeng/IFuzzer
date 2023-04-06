def walk_wrapper(walk_it):
    for dir_entry in walk_it:
        if dir_entry[0] == "aaa":
           yield dir_entry