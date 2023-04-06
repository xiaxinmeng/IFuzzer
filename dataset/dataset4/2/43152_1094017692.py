class FakeLog(list):
    def write(self, msg):
        self.append(msg)
    def flush(self):
        pass