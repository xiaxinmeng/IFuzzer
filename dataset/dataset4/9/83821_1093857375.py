
try:
    os.fdatasync(fd)
except Exception as err:
    logging.debug("fdatasync(fd) failed %s, falling back to fsync(fd)", err)
    os.fsync(fd)
