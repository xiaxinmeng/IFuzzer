class ForkWait(unittest.TestCase):
    ...
    def f(self, id):
        while not self.stop:
            self.alive[id] = os.getpid()
            try:
                time.sleep(SHORTSLEEP) <~~~ here
            except IOError:
                pass