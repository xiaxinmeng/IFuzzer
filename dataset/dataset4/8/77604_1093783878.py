import logging

app_logger = logging.getLogger('app')

app_logger.error('foo')
logging.error('goo')
app_logger.error('foo')