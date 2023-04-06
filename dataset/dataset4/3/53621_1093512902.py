def iterfind(elem, path, namespaces=None):
    # compile selector pattern
    if path[-1:] == "/":
        path = path + "*" # implicit all (FIXME: keep this?)