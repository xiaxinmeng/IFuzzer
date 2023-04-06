def samefile(f1, f2):
    "Test whether two pathnames reference the same actual file"
    return _getfinalpathname(f1) == _getfinalpathname(f2)