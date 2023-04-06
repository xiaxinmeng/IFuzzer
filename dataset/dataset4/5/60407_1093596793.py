def fullmatch(regex, input, flags=0):
    return re.match("(:?" + regex + ")$", input, flags)