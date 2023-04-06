class FlushFile(object):
    #"""Write-only flushing wrapper for file-type objects."""
    def __init__(self, f):
        self.f = f;
        self.flush = f.flush;
        try:
            self.encoding = f.encoding;
        except:
            pass;
    def write(self, x):
        self.f.write(x)
        self.f.flush()