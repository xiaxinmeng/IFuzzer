with self.subprocess_send_signal(pid, "SIGUSR1") as child: # here
    self.wait_signal(child, 'SIGUSR1', SIGUSR1Exception)