
def flush(self):
    # (Docstring skipped)
    if self.target:
        self.acquire()
        try:
            for record in self.buffer:
                self.target.handle(record)
            self.buffer.clear()
        finally:
            self.release()
