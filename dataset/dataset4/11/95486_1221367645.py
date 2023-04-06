def isreserved(path):
    """Return true if the pathname is reserved by the system."""
    # Refer to "Naming Files, Paths, and Namespaces":
    # https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    path = os.fsdecode(splitdrive(path)[1]).rstrip(r'\/')
    while path:
        path, name = split(path)
        if not name:
            break
        # '.' and '..' are not reserved.
        if name == '.' or name == '..':
            continue
        # Trailing spaces and dots are reserved.
        elif name.endswith((' ', '.')):
            return True
        # File streams are reserved (e.g. "filename:stream[:type]").
        elif ':' in name:
            return True
        # DOS device names are reserved (e.g. "nul" or "nul .txt"). The rules
        # are complicated and vary across Windows versions. On the side of
        # caution, return True for names that may not be reserved.
        elif name.partition('.')[0].rstrip(' ').upper() in _reserved_names:
            return True

    return False