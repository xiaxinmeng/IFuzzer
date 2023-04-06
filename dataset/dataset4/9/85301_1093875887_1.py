def is_macosx_sdk_path(path):
    """
    Returns True if 'path' can be located in an OSX SDK
    """
    return ( (path.startswith('/usr/') and not path.startswith('/usr/local'))
                or (path.startswith('/System/') and not path.startswith('/System/Volumes/Data'))
                or path.startswith('/Library/') )