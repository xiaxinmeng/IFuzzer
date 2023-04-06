def formatwarning(message, category, filename, lineno,
                  linec = []):
    """Function to format a warning the standard way."""
    s =  "%s:%s: %s: %s\n" % (filename, lineno, category.
__name__, message)
    if not linec:
        if imp.lock_held():
            # Somebody else is holding the import lock.  To avoid  
            # a deadlock we just return the string so in worst 
            # case the user can look it up themselves.  Sorry.
            return s
        else:
            import linecache
            linec.append(linecache.getline)
    line = linec[0](filename, lineno).strip()
    if line:
        s = s + "  " + line + "\n"
    return s