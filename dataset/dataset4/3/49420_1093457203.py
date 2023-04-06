import logging

logger = logging.getLogger('test_log')
logger.addHandler(logging.FileHandler('test.log', encoding='cp1251'))
logger.setLevel(logging.DEBUG)

logger.debug(u'Привет')    # russian Hello