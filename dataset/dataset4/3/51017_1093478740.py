if os.name == 'posix':
    import fcntl

    class file_wrapper:
        # Here we override just enough to make a file
        # look like a socket for the purposes of asyncore.
        # The passed fd is automatically os.dup()'d

        def __init__(self, fd):
            self.fd = os.dup(fd)

        def recv(self, *args):
            return os.read(self.fd, *args)

        def send(self, *args):
            return os.write(self.fd, *args)

        read = recv
        write = send

        def close(self):
            os.close(self.fd)

        def fileno(self):
            return self.fd