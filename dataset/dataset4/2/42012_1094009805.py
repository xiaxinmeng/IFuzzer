class addinfourlFixCyclRef(addinfourl):
    def close(self):
        if self.fp is not None and hasattr(self.fp, "_sock"):
            self.fp._sock.recv = None
        addinfourl.close(self)