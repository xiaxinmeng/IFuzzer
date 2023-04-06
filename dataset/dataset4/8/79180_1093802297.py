def log(log_level):
    pass


class Bot(object):
    def __init__(self):
        self.logger = None
        self.__init_logger(logging_level='INFO')
        self.logger.info('Initialized')
        self.logger.handlers = []  # remove all existing handlers
        self.__init_logger(logging_level='DEBUG')
        self.logger.debug('test')
        self.logger.info("Bot stopped.")

    def __init_logger(self, logging_level):
        self.logger = log(log_level=logging_level)