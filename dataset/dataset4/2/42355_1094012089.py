class PatchedLogger(logging.Logger):
    def __init__(self, name, *patches):
        logging.Logger.__init__(self, name)
        self.patches = patches
    def handle(self, record):
        #copied from the actual Logger implementation
        if (not self.disabled) and self.filter(record):
            for patch in self.patches:
                patch(record)
            self.callHandlers(record)