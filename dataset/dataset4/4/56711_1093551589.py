def handle_write_event(self):
    if self.accepting:
        # Accepting sockets shouldn't get a write event.
        # We will pretend it didn't happen.
        return