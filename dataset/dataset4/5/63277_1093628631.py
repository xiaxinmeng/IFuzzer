class TemporaryDirectory(object):
    def __init__(self, suffix="", prefix=template, dir=None):
        self.name = mkdtemp(suffix, prefix, dir)
        self._cleanup = weakref.finalize(self, shutil.rmtree, self.name)

    def __enter__(self):
        return self.name

    def __exit__(self, exc, value, tb):
        self._cleanup()

    def cleanup(self):
        self._cleanup()