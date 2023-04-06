import logging

logger = logging.getLogger(__name__)

def test():
    logger.debug('The result is ', 'abc')

def main():
    test()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()