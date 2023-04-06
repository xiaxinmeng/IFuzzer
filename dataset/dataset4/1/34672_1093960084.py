def escape(arg):
    import re
    # If arg contains no space or double-quote then
    # no escaping is needed.
    if not re.search(r'[ "]', arg):
        return arg
    # Otherwise the argument must be quoted and all
    # double-quotes, preceding backslashes, and
    # trailing backslashes, must be escaped.
    def repl(match):
        if match.group(2):
            return match.group(1) * 2 + '\\"'
        else:
            return match.group(1) * 2
    return '"' + re.sub(r'(\\*)("|$)', repl, arg) + '"'