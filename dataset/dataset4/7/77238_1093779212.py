import logging

class LogRecordTypeFilter(logging.Filter):
    def __init__(self, cls):
        self.cls = cls

    def filter(self, record):
        t = type(record)
        if t is not self.cls:
            msg = 'Unexpected LogRecord type %s, expected %s' % (t, self.cls)
            raise TypeError(msg)
        return True

class MyLogRecord(logging.LogRecord):
    pass

manager = logging.Manager(None)
manager.setLogRecordFactory(MyLogRecord)
logger = manager.getLogger('some_logger')
logger.addFilter(LogRecordTypeFilter(MyLogRecord))

try:
    logger.error('bpo-33057')
except TypeError as e:
    print(e)  # output: Unexpected LogRecord type <class 'logging.LogRecord'>, expected <class '__main__.MyLogRecord'>