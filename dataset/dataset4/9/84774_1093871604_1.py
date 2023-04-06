if base_parts[-1] != '':
    # the last item is not a directory, so will not be taken into account
    # in resolving the relative path
    del base_parts[-1]