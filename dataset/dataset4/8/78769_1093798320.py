def fill_stack(depth):
    if depth <= 1:
        return traceback.format_stack()
    else:
        return fill_stack(depth - 1)