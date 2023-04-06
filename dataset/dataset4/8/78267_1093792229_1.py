class CustomHandler(logging.Handler):
    def transmit(self, record):
        return False
    def emit(self, record):
        if not self.transmit(record):
            self.handleError(record)
def main():
    logger = logging.getLogger()
    logger.addHandler(CustomHandler())
    logger.warning('this will work in python 2.7, but not 3')

if __name__ == '__main__':
    main()