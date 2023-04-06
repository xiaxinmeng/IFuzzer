def run(self):
        while not self.finished.isSet():
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)