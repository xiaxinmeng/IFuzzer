class some_class(file):
    def __init__(self, arg):
        fd = do_some_os_stuff_with_forks_and_pipes_or_sockets
        return file.__init__(self, fd, 'r')

    def close(self):
        do_some_cleanup_stuff
        return file.close(self)