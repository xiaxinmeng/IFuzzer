
def send_signal(self, sig):
    """Send a signal to the process."""
    # Skip signalling a process that we know has already died.
    if self.returncode is None:
        os.kill(self.pid, sig)
