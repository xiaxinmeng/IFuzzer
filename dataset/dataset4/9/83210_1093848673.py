def clean(self):
    """Delete old files in "tmp"."""
    now = time.time()
    for entry in os.listdir(os.path.join(self._path, 'tmp')):
        path = os.path.join(self._path, 'tmp', entry)
        if now - os.path.getatime(path) > 129600:   # 60 * 60 * 36
            os.remove(path)