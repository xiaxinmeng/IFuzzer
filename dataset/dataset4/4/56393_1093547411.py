for child in self.active_children:
    os.waitpid(child, os.WNOHANG)