def _isdir(dirname):
    """os.path.isdir() doesn't work for UNC mount points. 
Fake it.
    
    # For an existing mount point
    # (want: _isdir() == 1)
    os.path.ismount(r"\\crimper\apps") -> 1
    os.path.exists(r"\\crimper\apps") -> 0
    os.path.isdir(r"\\crimper\apps") -> 0
    os.listdir(r"\\crimper\apps") -> [...contents...]
    # For a non-existant mount point
    # (want: _isdir() == 0)
    os.path.ismount(r"\\crimper\foo") -> 1
    os.path.exists(r"\\crimper\foo") -> 0
    os.path.isdir(r"\\crimper\foo") -> 0
    os.listdir(r"\\crimper\foo") -> WindowsError
    # For an existing dir under a mount point
    # (want: _isdir() == 1)
    os.path.mount(r"\\crimper\apps\Komodo") -> 0
    os.path.exists(r"\\crimper\apps\Komodo") -> 1
    os.path.isdir(r"\\crimper\apps\Komodo") -> 1
    os.listdir(r"\\crimper\apps\Komodo") -> [...contents...]
    # For a non-existant dir/file under a mount point
    # (want: _isdir() == 0)
    os.path.ismount(r"\\crimper\apps\foo") -> 0
    os.path.exists(r"\\crimper\apps\foo") -> 0
    os.path.isdir(r"\\crimper\apps\foo") -> 0
    os.listdir(r"\\crimper\apps\foo") -> []  # as if empty 
contents
    # For an existing file under a mount point
    # (want: _isdir() == 0)
    os.path.ismount(r"\\crimper\apps\Komodo\exists.txt") -> 
0
    os.path.exists(r"\\crimper\apps\Komodo\exists.txt") -> 1
    os.path.isdir(r"\\crimper\apps\Komodo\exists.txt") -> 0
    os.listdir(r"\\crimper\apps\Komodo\exists.txt") -> 
WindowsError
    """
    if sys.platform[:3] == 'win' and dirname[:2] == r'\\':
        if os.path.exists(dirname):
            return os.path.isdir(dirname)
        try:
            os.listdir(dirname)
        except WindowsError:
            return 0
        else:
            return os.path.ismount(dirname)
    else:
        return os.path.isdir(dirname)