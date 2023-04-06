for tarinfo in tar:
    if tarinfo.islnk():
        tar.extract(tarinfo)