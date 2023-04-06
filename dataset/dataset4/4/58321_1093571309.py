if category == LC_ALL and ';' in localename:
    raise TypeError('category LC_ALL is not supported')