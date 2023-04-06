class ThreadSignals(unittest.TestCase):
    def test_signals(self):
        signalled_all.acquire()
        self.spawnSignallingThread()
        signalled_all.acquire() <~~~~ here