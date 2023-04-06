my_logger = logging.getLogger('MyLogger')  # logger is singleton
my_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':

    handler = logging.handlers.SysLogHandler(address=('192.168.1.23', 514), facility="auth", socktype=socket.SOCK_STREAM)
    my_logger.addHandler(handler)
    my_logger.critical('this is critical')

    handler.flush()
    handler.close()
    my_logger.removeHandler(handler)