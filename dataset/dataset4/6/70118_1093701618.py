
def rmtree(path):
    """On windows, rmtree fails for readonly dirs."""
    def handle_remove_readonly(func, path, exc):  # pragma: no cover (windows)
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            func(path)
        else:
            raise
    shutil.rmtree(path, ignore_errors=False, onerror=handle_remove_readonly)
