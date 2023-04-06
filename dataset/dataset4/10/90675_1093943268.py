if len(query) and not isinstance(query[0], tuple):
    raise TypeError("not a valid non-string sequence "
                    "or mapping object")