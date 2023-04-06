class PatchedSharedFile(zipfile._SharedFile):
    def __init__(self, *args):
        super().__init__(*args)
        self.tell = lambda: self._pos
zipfile._SharedFile = PatchedSharedFile