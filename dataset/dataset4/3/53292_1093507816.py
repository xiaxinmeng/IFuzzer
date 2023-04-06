def is_macosx_sdk_path(path):
    """
    Returns True if 'path' can be located in an OSX SDK
    """
    return path.startswith('/usr/') or path.startswith('/System/')