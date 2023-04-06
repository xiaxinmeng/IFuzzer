
import os
import logging.config

logging.config.fileConfig('logging.ini', defaults=os.environ)
logger = logging.getLogger(__name__)
logger.debug('debug msg')
logger.info('info msg')
logger.warn('warn msg')
logger.error('error msg')
root_logger = logging.getLogger()
print('root_logger.level = %d; logging.WARN = %d; logging.DEBUG = %d'
      % (root_logger.level, logging.WARN, logging.DEBUG))
