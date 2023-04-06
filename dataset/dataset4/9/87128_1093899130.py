@unittest.removeHandler
def test_signal_handlers_installed(self):
    SIG = signal.SIGINT
    if sys.platform == 'win32':
        SIG = signal.CTRL_C_EVENT
    with self.assertRaises(KeyboardInterrupt):
        os.kill(os.getpid(), SIG)
        if sys.platform == 'win32':
            time.sleep(.1)  # Give handler's thread time to join