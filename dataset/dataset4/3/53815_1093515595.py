import logging
class Filter(object):
    def filter(self, record):
        return record.name == 'foo'  
logger = logging.getLogger()
formatter = logging.Formatter('%(message)s') 
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addFilter(Filter())
logger.addHandler(handler)
logging.getLogger('foo').warn('foo!')
logging.getLogger('bar').warn('bar!')