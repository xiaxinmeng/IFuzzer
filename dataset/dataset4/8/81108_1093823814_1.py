def format_tb(tb, limit=None):
    """A shorthand for 'format_list(extract_tb(tb, limit))',
    which returns a list of strings ready for printing'.
    """
    return extract_tb(tb, limit=limit).format()