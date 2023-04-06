def addpackage(sitedir, name, known_paths):
    if known_paths is None:
        known_paths = _init_pathinfo()
        reset = True
    else:
        reset = False
    fullname = os.path.join(sitedir, name)
    try:
        # here should set the second param as encoding='utf-8'
        f = open(fullname, "r")
    except OSError:
        return
    # other codes