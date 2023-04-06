start_method = get_start_method()
if start_method is None:
    set_start_method('forkserver')