            # in the case of paths with these prefixes:
            # \\.\ -> device names
            # \\?\ -> literal paths
            # do not do any normalization, but return the path
            # unchanged apart from the call to os.fspath()