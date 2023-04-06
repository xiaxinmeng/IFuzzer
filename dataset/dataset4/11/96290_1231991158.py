path = get_path_for_this_demo()
while path:
    do_something_with_path(path)
    path = os.path.dirname(path)